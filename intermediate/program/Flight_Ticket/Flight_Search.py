# TODO 2. 항공편 DATA 가져오기
#구글시트에서 변수 가져오기 : 공항이름
from datetime import *
import requests
from dateutil.relativedelta import relativedelta
from Flight_Data import FlightData

flight_search_api = "https://tequila-api.kiwi.com"
flight_api_key = ""

headers = {
    "apikey":flight_api_key
}
class FlightSearch:

    # TODO 3.항공코드 가져오기
    # USER가 관리하는 설정 DATA 얻기 함수 - GET
    #https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
    def get_iata_code(self, city_name):
        IATA_CODE_API = f"{flight_search_api}/locations/query"
        iata_code_params = {
            "term" : city_name,
            "location_types" : "city"
        }
        iata_code_response = requests.get(url=IATA_CODE_API, params=iata_code_params, headers=headers)
        code = iata_code_response.json()["locations"][0]["code"]
        return code

    # TODO 4. 항공편 DATA 가져오기
    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_search_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        flight_search_response = requests.get(url=f"{flight_search_api}/v2/search", params=flight_search_params, headers=headers)
        print(flight_search_response.text)

        try:
            data = flight_search_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data







