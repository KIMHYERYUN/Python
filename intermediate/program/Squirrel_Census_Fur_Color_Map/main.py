import pandas as pd

#csv 파일 읽기
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#특정 색깔의 다람쥐 관련 행 가져오기
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]
red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
#print(grey_squirrel)
#개체 수 확인하기
#print(grey_squirrel.count())
#print(len(grey_squirrel))
grey_squirrel_count = len(grey_squirrel)
black_squirrel_count = len(black_squirrel)
red_squirrel_count = len(red_squirrel)

#dataframe 만들기 - dict 형태
data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count" : [grey_squirrel_count, black_squirrel_count, red_squirrel_count]
}
print(data_dict)
#{'Fur Color': ['Gray', 'Black', 'Cinnamon'], 'Count': [2473, 103, 392]}

#dict -> dataframe 형태로
df = pd.DataFrame(data_dict)
#csv로 저장
df.to_csv("squirrel_count.csv")