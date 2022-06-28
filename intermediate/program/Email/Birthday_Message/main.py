##################### Hard Starting Project ######################
import smtplib

from pandas import DataFrame
import pandas
import datetime
import random

MY_EMAIL = "90x619@gmail.com"
PASSWORD = ""


#오늘 날짜 가져오기
now = datetime.datetime.now()
today_tuple = (now.month, now.day)

'''
#csv파일 열고 읽어서 dict 형태로 가져오기
birthday_data = pandas.read_csv("birthdays.csv")
birthday_data_dict = DataFrame.to_dict(birthday_data, orient="records")
print(birthday_data_dict)
#[{'name': 'KHR', 'email': '90x619@gmail.com', 'year': 1990, 'month': 6, 'day': 19}, {'name': 'PBJ', 'email': 'jaydenkhr@gmail.com', 'year': 1962, 'month': 5, 'day': 30}, {'name': 'HUR', 'email': 'kimheyryun@naver.com', 'year': 1988, 'month': 5, 'day': 31}]
'''
#csv 파일을 열고
birthday_data = pandas.read_csv("birthdays.csv")
#각 열의 month와 day 가져오기
#각 열을 불러 인덱스로 잡혀있는 row를 가져와 row에 있는 month와 day를 dictionary 형태로 묶기
#birthday_data_dict = {(birthday_month, birthday_day):birthday_data_row}
#birthday_data_dict = {data_row.month: data_row.day for (index, data_row) in birthday_data.iterrow()}
birthday_data_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in birthday_data.iterrows()}
print(birthday_data_dict)
'''
{(6, 19): name                  KHR
email    90x619@gmail.com
year                 1990
month                   6
day                    19
Name: 0, dtype: object, (5, 30): name                     PBJ
email    jaydenkhr@gmail.com
year                    1962
month                      5
day                       30
Name: 1, dtype: object, (5, 31): name                      HUR
email    kimheyryun@naver.com
year                     1988
month                       5
day                        31
Name: 2, dtype: object}
'''
#생일과 오늘의 날짜가 같은 경우
if today_tuple in birthday_data_dict:
    # 랜덤 메시지 고르기
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt") as letter_templates_file:
        letter_templates = letter_templates_file.read()
        # 이름 가져오기 - 오늘 생일인 키를 가진 사람 구하기
        birthday_person = birthday_data_dict[today_tuple]
        birthday_person_name = birthday_person["name"]
        birthday_msg = letter_templates.replace("[NAME]", birthday_person_name)

    try:
        with smtplib.SMTP("smtp.google.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="90x619@gmail.com", msg=f"Subject:Happy Birthdya!\n\n {birthday_msg}")
            connection.close()
    except TimeoutError as error_message:
        print(error_message)
