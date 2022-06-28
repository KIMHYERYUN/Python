import requests

user_firstname = input("Welcome to KHR'S Flight Club!\n We find the best flight deals and email you.\n What's your first name?\n")
user_lastname = input(" What's your last name?\n")
user_email = input(" What's your email?\n")
user_email_check = input(" Type your email agian.\n")
if user_email == user_email_check:
    print("You're in the club!")

#TODO +. USER가 입력한 정보 업데이트
users_sheet_api = "https://api.sheety.co/06c6a40627b3852f5d250d9baf3ebc19/flightPrices/users"

users_sheet_request = requests.post(url=users_sheet_api, json=user)