#TODO 1. 항공권 검색 API 가져오기 - https://tequila.kiwi.com/portal/docs/tequila_api - POST
import datetime
from datetime import *
from pprint import pprint
import requests
from dateutil.relativedelta import relativedelta

flight_search_api = "https://tequila-api.kiwi.com"
flight_api_id = ""
flight_api_key = ""

headers = {
    "apikey":flight_api_key
}


SETTING_API = "https://api.sheety.co/06c6a40627b3852f5d250d9baf3ebc19/flightPrices/flightprice"

SETTING_USERNAME = ""
SETTING_PASSWORD = ""


class DataManager:
    def __init__(self):
        self.setting_data_result = {}


    #TODO 2. USER가 관리하는 설정 DATA 가져오기 - 함수, GET

    def get_data(self):
        setting_response = requests.get(url=SETTING_API, auth=(SETTING_USERNAME, SETTING_PASSWORD))
        setting_data = setting_response.json()
        self.setting_data_result = setting_data["flightprice"]
        return self.setting_data_result
        #설정 DATA 자동배열
        #pprint(setting_data_result)

    '''
    {'flightprice': [{'city': 'Los Angeles', 'iataCode': 'LAX', 'lowestPrice': 1000, 'id': 2},
                     {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 900, 'id': 3},
                     {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 800, 'id': 4},
                     {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 400, 'id': 5},
                     {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 500, 'id': 6},
                     {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 1200, 'id': 7},
                     {'city': 'Toronto', 'iataCode': 'YYZ', 'lowestPrice': 800, 'id': 8}]}
    '''


    #TODO 3. USER가 관리하는 설정 DATA 업데이트 - 함수 - PUT - IATA CODE
    UPDATE_SETTING_API = "https://api.sheety.co/06c6a40627b3852f5d250d9baf3ebc19/flightPrices/flightprice/[Object ID]"

    def update_iata_code(self):
        for city in self.setting_data_result:
            new_data = {
                "flightprice" : {
                    "iataCode": city["iataCode"]
                    }
                }
            update_response = requests.put(url=f"{SETTING_API}/{city['id']}",
                                               json=new_data)
            print(update_response.text)



    '''
    {'flightprice': [{'city': 'Los Angeles',
                      'iataCode': 'LAX',
                      'id': 2,
                      'lowestPrice': 1000},
                     {'city': 'Paris',
                      'iataCode': 'PAR',
                      'id': 3,
                      'lowestPrice': 900},
                     {'city': 'Berlin',
                      'iataCode': 'BER',
                      'id': 4,
                      'lowestPrice': 800},
                     {'city': 'Sydney',
                      'iataCode': 'SYD',
                      'id': 5,
                      'lowestPrice': 400},
                     {'city': 'Istanbul',
                      'iataCode': 'IST',
                      'id': 6,
                      'lowestPrice': 500},
                     {'city': 'New York',
                      'iataCode': 'NYC',
                      'id': 7,
                      'lowestPrice': 1200},
                     {'city': 'Toronto',
                      'iataCode': 'YYZ',
                      'id': 8,
                      'lowestPrice': 800}]}
    '''