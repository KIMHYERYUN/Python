#OPEN API : http://open-notify.org/Open-Notify-API/ISS-Location-Now/
#https://sunrise-sunset.org/api
from datetime import datetime

import requests

MY_LAT = 37.566536
MY_LONG = 126.977966

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
#예외 상태 코드
response.raise_for_status()

data = response.json()
print(data)
#{'results': {'sunrise': '8:10:18 PM', 'sunset': '10:50:05 AM', 'solar_noon': '3:30:12 AM',
# 'day_length': '14:39:47', 'civil_twilight_begin': '7:41:10 PM', 'civil_twilight_end': '11:19:14 AM',
# 'nautical_twilight_begin': '7:03:00 PM', 'nautical_twilight_end': '11:57:23 AM',
# 'astronomical_twilight_begin': '6:20:20 PM', 'astronomical_twilight_end': '12:40:03 PM'}, 'status': 'OK'}


#https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=2022-05-16
#위의 형식으로 json?뒤 대입하면 출력가능
#https://api.sunrise-sunset.org/json?lat=37.566536&lng=-126.977966&date=2022-06-03
'''
{
"results": {
"sunrise": "1:05:55 PM",
"sunset": "3:46:21 AM",
"solar_noon": "8:26:08 PM",
"day_length": "14:40:26",
"civil_twilight_begin": "12:36:44 PM",
"civil_twilight_end": "4:15:32 AM",
"nautical_twilight_begin": "11:58:31 AM",
"nautical_twilight_end": "4:53:46 AM",
"astronomical_twilight_begin": "11:15:44 AM",
"astronomical_twilight_end": "5:36:32 AM"
},
"status": "OK"
}
'''
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
#formatted 삽입 전
#8:10:18 PM
#10:50:05 AM
#formatted 삽입 후
#2022-06-02T20:10:18+00:00
#2022-06-03T10:50:05+00:00

time_now = datetime.now()
print(time_now)
#2022-06-03 11:30:12.052262

#형식 맞추기
sunrise_form = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_form = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_form)
print(sunset_form)
print(time_now.hour)



