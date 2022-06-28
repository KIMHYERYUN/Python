#리스트와 dictionary 차이
#표현방식
#list : []
#dic : {}

#index
#list : index 숫자
#dic : key


#Nesting
#{key1:[List],key2:{dictionary}}
cbg_bluetals ={"Korea" : "Seoul", "America":"Newyork","France":"Paris"}

#Nesting a list in a Dictionary
travel_log = {"Korea" : ["Seoul", "Gyeonggido", "Jeju"],
              "America": ["La", "Sanfransico", "Newyork"]}

#Nesting a dictionary in a Dictionary
#cities_visited라는 키값의 리스트를 값으로 갖도록
travel_log = {"Korea" : {"cities_visited": ["Seoul", "Gyeonggido", "Jeju"], "total_visits":12},
              "America": {"cities_visited": ["La", "Sanfransico", "Newyork"], "total_visits":5}}

#Nesting a dictionary in a List
#[{key:[List], key2:{Dict}}, {key1:value1, key2:value2}]
travel_log = [{"country":"Korea",
               "cities_visited": ["Seoul", "Gyeonggido", "Jeju"],
               "total_visits":12},
              {"country":"America",
               "cities_visited": ["La", "Sanfransico", "Newyork"],
               "total_visits":5}]

#steak 출력하기 위한 코드
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])
# steak가 있는 곳은 리스트이기때문에 [0] 필요