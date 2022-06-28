# camelcamelcamel - 가격변동 확인사이트


# 추적상품 : https://www.amazon.com/Durgod-Taurus-Mechanical-Gaming-Keyboard/dp/B07QK16RDQ/ref=sr_1_15?keywords=keychron+red+switch+keyboard&qid=1655793117&sprefix=keychron+red%2Caps%2C420&sr=8-15

##아마존 - 특정상품 외 다른 정보들도 많이 전달 --> 허데 포함해야함 : http://myhttpheader.com에서 확인

import requests
from bs4 import BeautifulSoup
import lxml

amazon_url = "https://www.amazon.com/Durgod-Taurus-Mechanical-Gaming-Keyboard/dp/B07QK16RDQ/ref=sr_1_15?keywords=keychron+red+switch+keyboard&qid=1655793117&sprefix=keychron+red%2Caps%2C420&sr=8-15"
headers = {'Accept-Language': "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
# TODO 1. 가격정보 가져오기
# 아마존 정보 요청
response = requests.get(url=amazon_url, headers=headers)
amazon_data = response.text
# print(amazon_data)

# HTML 형태 변환
soup = BeautifulSoup(amazon_data, "lxml")
print(soup.prettify())

# 가격정보 가져오기
price_tag = soup.find(name="span", class_="a-offscreen")
print(price_tag)
# <span class="a-offscreen">$124.99</span>

price_text = price_tag.get_text()
print(price_text)
# $124.99

price_float = float(price_text.split("$")[1])
print(price_float)

# 상품이름 가져오기
product = soup.find(id="productTitle").get_text().replace(" ", "")
print(product)

# TODO 2. 설정가격 이하 시 메일보내기

import smtplib

MY_EMAIL = "90x619@gmail.com"
MY_PASSWORD = "rspiqjrqnwcrymfc"
TO = "90x619@gmail.com"
Text = f"Subject: Price down!!\n\n You have to buy it. This product price is {price_float}. Hurry up! Click here : {amazon_url}"

PRICE_LIMIT = 125

if price_float < PRICE_LIMIT:
    message = f"{product} is price down"

    try:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO, msg=Text)
            connection.close()
    except TimeoutError as error_message:
        print(error_message)

#TODO 3. 2022.5.30구글정책 변경에 따라 접근불가 : 2단계 인증 후 임시 앱 비밀번호 생성 후 사용
#변경완료 - 해결완료