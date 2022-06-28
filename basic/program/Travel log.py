travel_log = [
{
  "country": "Korea",
  "visits": 12,
  "cities": ["Jeju", "Jinju", "Sokcho"]
},
{
  "country": "America",
  "visits": 5,
  "cities": ["LA", "Sanfrancisco", "Newyork"]
},
]

#List에 추가
def add_new_country(country, visits, cities):
  travel_log.append({"country" : country, "visits" : visits, "cities" : cities})

  #다른 방법
  #new_country={}
  #new_country["country"] = country
  #new_country["visits"] = visits
  #new_country["cities"] = cities
  #travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#[{'country': 'Korea', 'visits': 12, 'cities': ['Jeju', 'Jinju', 'Sokcho']}, {'country': 'America', 'visits': 5, 'cities': ['LA', 'Sanfrancisco', 'Newyork']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}]

