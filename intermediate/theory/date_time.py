#datetime : 날짜와 시간 형식화
#year, weekday, month....

import datetime as dt

#datetime 클래스
now = dt.datetime.now()
print(now)
#2022-05-30 04:12:50.478868

#오류 : ImportError: cannot import name 'datetime' from partially initialized module 'datetime' (most likely due to a circular import) (C:\Works\workspace\intermediate\basic\datetime.py)
#이유 : 파일명 datetime - 혼란


year = now.year
print(type(now))
print(type(year))
#<class 'datetime.datetime'>
#<class 'int'>

day_of_week = now.weekday()
print(day_of_week)
#0 -> 첫번째 주

#생일 저장하기
date_of_birth = dt.datetime(year=1990, month=6, day=19, hour=23, minute=45)
print(date_of_birth)
#1990-06-19 23:45:00


#형식 바꾸기 : strftime
#%각 약자 => 참고