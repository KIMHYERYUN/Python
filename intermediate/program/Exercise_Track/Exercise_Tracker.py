# API = https://www.nutritionix.com/business/api
# TODO 0. 모듈 생성
from datetime import *
import os

import requests

# TODO 0. 변수 생성
COMB_API_ID = ""
COMB_API_KEY = ""

headers = {
    "x-app-id": COMB_API_ID,
    "x-app-key": COMB_API_KEY
}

EXERCISE_TEXT = input("Which exercise you did? ")
GENDER = "female"
WEIGHT = "59.5"
HEIGHT = "166.8"
AGE = "32"

USER_NAME=""
USER_PASSWORD=""


# TODO 2. 운동입력 - 자연어처리
post_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

post_exercise_parameters = {
    "query" : EXERCISE_TEXT,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE,
}

post_response = requests.post(url=post_exercise_endpoint, json=post_exercise_parameters, headers=headers)
post_response_json = post_response.json()
print(post_response_json)
'''
{'exercises': [{'tag_id': 317, 'user_input': 'running', 'duration_min': 20, 'met': 7.5, 'nf_calories': 150,
                'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
                          'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg',
                          'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None,
                'benefits': None}]}
'''

# TODO 3. 입력된 값 구글시트에 저장 - sheety - POST
add_row_endpoint = "https://api.sheety.co/06c6a40627b3852f5d250d9baf3ebc19/workoutsTrecking/workouts"


#입력 값
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X %p")

for exercise in post_response_json["exercises"]:
    add_row_parameters = {
        "workout" : {
            "date": today_date,
            "time": now_time,
            #title : 첫글자 대문자
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
#권한있는 경우-BASIC
post_response_add = requests.post(url=add_row_endpoint, json=add_row_parameters,
                                  auth=(USER_NAME, USER_PASSWORD)
                                    )
'''
#권한없는 경우
post_response_add = requests.post(url=add_row_endpoint, json=add_row_parameters)
#권한있는 경우-BEARER TOKEN : 토큰 운반자에게 권한 부여
TOKEN = ""
bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}
sheet_response = requests.post(url=add_row_endpoint, json=add_row_parameters,
                               headers=bearer_headers)
'''
print(post_response_add.text)