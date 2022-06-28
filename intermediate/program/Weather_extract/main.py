with open("./weather_data.csv") as weather_data:
    weather_datas = weather_data.readlines()
    print(weather_datas)
    #['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n',
    #'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

#각 행과 열을 분리하기 위한 작업 - 내장 라이브러리
import csv

with open("weather_data.csv") as weather_data:
    weather_datas = csv.reader(weather_data)
    print(weather_datas)
    #<_csv.reader object at 0x00000231AE6285E0> : csv.reader의 객체 생성 주소
    #각 온도 추출
    temperatures = []
    for row in weather_datas:
        #print(row)
        '''
        ['day', 'temp', 'condition']
        ['Monday', '12', 'Sunny']
        ['Tuesday', '14', 'Rain']
        ['Wednesday', '15', 'Rain']
        ['Thursday', '14', 'Cloudy']
        ['Friday', '21', 'Sunny']
        ['Saturday', '22', 'Sunny']
        ['Sunday', '24', 'Sunny']
        '''
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
    #['12', '14', '15', '14', '21', '22', '24']

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
'''
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
'''

#data의 column명을 통해 불러올 수 있음
print(data["temp"])
'''
0    12
1    14
2    15
3    14
4    21
5    22
6    24'''

#pandas를 통한 데이터 타입형태 : dataframe
print(type(data))
'''Name: temp, dtype: int64
<class 'pandas.core.frame.DataFrame'>'''

#데이터 타입형태 변환 : dataframe - dict
print(data.to_dict())
#{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

#데이터 타입형태 변환 : series - list
print(data['temp'].to_list())
#[12, 14, 15, 14, 21, 22, 24]


#평균온도 구하기
#방법 1
list_temp = data['temp'].to_list()
sum_temp = 0
for temp in list_temp:
    sum_temp += temp

average_1 = sum_temp / len(list_temp)
print(average_1)

#방법 2
average_2 = sum(list_temp) / len(list_temp)
print(average_2)

#방법 3
average_3 = data["temp"].mean()
print(average_3)


#최고값
print(data["temp"].max())
#오류 : 'list' object has no attribute 'max' - 리스트 내에서 max 함수 사용불가
#print(list_temp.max())


#각 열을 요소처럼 불러올수있음
print(data["condition"])
print(data.condition)
'''
0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
Name: condition, dtype: object
'''


#가장 높은 온도의 행 찾기
print(data[data.temp == data.temp.max()])
'''
      day  temp condition
6  Sunday    24     Sunny
'''

#월요일의 온도 구하기
monday = data[data.day == "Monday"]
monday_temp = monday.temp
monday_temp_fahrenheit = (int(monday_temp) * 9/5) + 32
#int로 미변환 시 그대로 series 형태로 남음
print(monday_temp_fahrenheit)


#scratch - dataframe 만들기
data_dict = {"student":["Kim", "Hur", "Park"],
            "score":[91, 88, 79]}
data_dataframe = pandas.DataFrame(data_dict)
print(data_dataframe)
'''
  student  score
0     Kim     91
1     Hur     88
2    Park     79
'''

#dataframe - csv 파일도 만들기
data_csv = data_dataframe.to_csv("score_data.csv")
