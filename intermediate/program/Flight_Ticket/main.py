from datetime import *
from dateutil.relativedelta import relativedelta
from Data_Manager import DataManager
from Flight_Search import FlightSearch
from Send_SMS import SendSMS

data_manager = DataManager()
data = data_manager.get_data()
flight_search = FlightSearch()
send_sms = SendSMS()

AIRPORT_NAME = "LAX"
KNOW_MONTH = 6

TOMORROW_DATE = datetime.now() + timedelta(days=KNOW_MONTH*30)
TOMORROW_DATE_FORMATEED = TOMORROW_DATE.strftime("%d/%m/%Y")
#print(TODAY_DATE)

#방법1 : relativedelta 모듈 활용
AFTER_DATE = TOMORROW_DATE + relativedelta(months=+KNOW_MONTH)
AFTER_DATE_FORMATTED = AFTER_DATE.strftime("%d/%m/%Y")
#방법2 : banker's definition
#AFTER_DATE = TODAY_DATE + datetime.timedelta(KNOW_MONTH * 30)

# TODO 5. 구글시트에 IATA Code가 없는경우 입력
if data[0]["iataCode"] == "":
    city_names = [row["city"] for row in data]
    codes = flight_search.get_iata_code(city_names)
    data_manager.update_iata_code()
    data = data_manager.get_data()
    #for row in data:
    #    row["iataCode"] = data_manager.get_iata_code(row["city"])
    #print(data)

# TODO 6. 항공권 검색
for destination in data:
    flight = flight_search.check_flight(
        origin_city_code=AIRPORT_NAME,
        destination_city_code=destination["iataCode"],
        from_time=TOMORROW_DATE_FORMATEED,
        to_time=AFTER_DATE_FORMATTED
    )

    # TODO 7. 항공권 금액 중 상한선 이하 발생 시 SMS
    if flight.price < destination["lowestPrice"]:
        send_sms.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
