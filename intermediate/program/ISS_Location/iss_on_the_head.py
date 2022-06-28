#============================iss position================================
import datetime
import time

import requests
import smtplib
#============================my position==================================

MY_LAT = 37.566536
MY_LONG = 126.977966

#=============================over head=====================================
def is_over():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    iss_latiitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]
    print(iss_latiitude)
    print(iss_longitude)


    if MY_LAT-5 <= iss_latiitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <=MY_LONG+5:
        return True

#============================night check====================================
def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_form = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_form = data["results"]["sunset"].split("T")[1].split(":")[0]

    #현재 시각
    time_now = datetime.now().hour

    #밤이 어두운 조건
    if time_now >= sunset_form or time_now <= sunrise_form:
        return True

#====================email sending=========================================

MY_EAMIL = "90x619@gmail.com"
MY_PASSWORD = ""

while True:
    #반복해서 일어나는 스크립트 실행 간 대기시간 설정
    time.sleep(60)
    if is_over() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EAMIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EAMIL, to_addrs=MY_EAMIL, msg="Subject:Look Up\n\nThe ISS is above you in the sky.")
