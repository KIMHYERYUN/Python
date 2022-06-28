#API : PIXELA 데이터 업로드 - 추적

# TODO 1. 사용자 계정 생성
from datetime import *

import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_name = ""
token = ""

user_params = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#게시하는 데이터 대부분 JSON 형식 - 전송하려는 json 데이터
response = requests.post(url=pixela_endpoint, json=user_params)
#성공여부만 확인하기 위해
print(response.text)
#{"message":"Success. Let's visit https://pixe.la/@kimhyeryun , it is your profile page!","isSuccess":true}

# TODO 2. 그래프 생성

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

graph_id = "khrgraph1"

graph_parameter = {
    "id": graph_id,
    "name":"Cycling",
    "unit": "Kilometer",
    "type": "float",
    "color": "sora",
}

#자신을 인증하는 방법
headers = {
    "X-USER-TOKEN": token
}

#graph_response = requests.post(url=graph_endpoint, json=graph_parameter, headers=headers)
#print(graph_response.text)
#오류 : {"message":"User `kimhyeryun` does not exist or the token is wrong.","isSuccess":false} - header 추가필요
#{"message":"Success.","isSuccess":true}

#https://pixe.la/v1/users/kimhyeryun/graphs/khrgraph1.html

# TODO 3. 픽셀 생성
post_pixel_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

post_pixel_parameter = {
    #"date": "20220605",
    "date" : today_formatted,
    "quantity" : input("How many kilometers did you cycle today? "),
}

post_pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameter, headers=headers)
print(post_pixel_response.text)
#{"message":"Success.","isSuccess":true}


# TODO 4. 픽셀 업데이트 - PUT
put_pixel_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}/{today_formatted}"

put_pixel_parameters = {
    "quantity" : "13.59"
}

#put_pixel_response = requests.put(url=put_pixel_endpoint, json=put_pixel_parameters, headers=headers)
#print(put_pixel_response.text)
#{"message":"Success.","isSuccess":true}


# TODO 5. 픽셀 삭제하기 - DELETE
delete_pixel_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}/{today_formatted}"

#delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
#print(delete_pixel_response.text)
#{"message":"Success.","isSuccess":true}


# TODO 6. 픽셀 추적하기 - RESPONSE OFF, CREATE PIXEL : INPUT
##추적하고자 하기 위해서는 response를 다 닫고, 새로 생성하는 곳에 input