#Beautiful + Selenium

#zillow 조건 - 웹 스크랩핑 - google form - excel data 축적 - spread sheet extract

#TODO 0. 구글 폼 만들기
import time

from selenium import webdriver

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfhSPCnKAZxCnbMkOunx6ThU-QnqAjvJhBm--ld81YFJHRuzg/viewform?usp=sf_link"

ZILLOW_URL = "https://www.zillow.com/homes/for_sale/house,condo,mobile,townhouse,apartment_type/1-_beds/1.0-_baths/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-118.41544375913207%2C%22east%22%3A-116.80869327085082%2C%22south%22%3A33.313478059122694%2C%22north%22%3A34.18924676171046%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A200000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A918%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22built%22%3A%7B%22min%22%3A2010%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

#TODO 1. 리스트 가져오기 - Beautiful Soup - 주소, 가격, 링크 리스트 만들기
from bs4 import BeautifulSoup
import requests

#http://myhttpheader.com/
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language" : "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

#TODO 1-1.requests/response
response = requests.get(url=ZILLOW_URL, headers=headers)
data = response.text
soup = BeautifulSoup(data, "html.parser")

#TODO 1-2. 모든 링크 가져오기
all_link_elements = soup.select(".list-card-top a")
print(all_link_elements)
#출력값 : 각 링크가 포함된 전체 태그 - 리스트화

all_link = []
for link in all_link_elements:
    link_address = link["href"]
    all_link.append(link_address)

#TODO 1-3. 모든 주소 가져오기
all_address = []
all_address_elements = soup.select(".list-card-info address")
print(all_address_elements)
for address in all_address_elements:
    address_text = address.get_text()
    all_address.append(address_text)

#TODO 1-4. 모든 가격 가져오기
all_price = []
all_price_elements = soup.select(".list-card-price")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements]




#TODO 2. 데이터 입력하기 - Selenium

CHROME_DRIVER_PATH = "C:\projects\chromedriver\chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

#TODO 2. 각 링크를 열어 구글폼  - 가져온 모든 링크에 대해 구글폼 입력 제출
for n in range(len(all_link)):
    driver.get(GOOGLE_FORM)

    time.sleep(2)

    address = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")

    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    address.send_keys(all_address[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_link[n])
    submit_button.click()




#TODO 1-
#TODO 1-
#TODO 1-
