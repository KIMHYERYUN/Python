#pandas : 분석 라이브러리, 설치 필요
#pandas.pydata.org/docs : 각 형태 변환함수 등
# import pandas
#
# data = pandas.read_csv("./program/Weather_extract/weather_data.csv")
# print(data)
#
# #data의 column명을 통해 불러올 수 있음
# print(data["temp"])
# #pandas를 통한 데이터 타입형태 : dataframe
# print(type(data))

#pandas의 데이터 구조 : series(1차원-리스트와 같은), dataframe(2차원)

#program > Weather_extract > weather_data.csv 참고

#scratch - dataframe 만들기
import pandas

data_dict = {"student":["Kim", "Hur", "Park"],
            "score":[91, 88, 79]}
print(pandas.DataFrame(data_dict))




#data["데이터의 열의 모든값"]
#data.데이터 열의 원소값