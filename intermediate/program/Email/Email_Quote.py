import datetime
import smtplib
import random

#나의 이메일 정보
my_email = "90x619@gmail.com"
password = ""

#현재 요일
now = datetime.datetime.now()
day_of_week =now.weekday()
print(day_of_week)

#매주 월요일에 보내기 - monday = 0 부터
if day_of_week == 0:
    #연결
    #connection = smtplib.SMTP("smtp.google.com")
    # 메일 보낼 내용 추출
    with open("quotes.txt") as quote_file:
        # 각 줄 읽어오기
        all_quotes = quote_file.readlines()
        # 랜덤 추출
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.google.com", port=587) as connection:
        #서버연결
        connection.starttls()
        #로그인
        connection.login(user=my_email, password=password)
        #메일 보내기
        connection.sendmail(from_addr=my_email,
                            to_addrs="jaydenkhr@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")
        connection.close()

