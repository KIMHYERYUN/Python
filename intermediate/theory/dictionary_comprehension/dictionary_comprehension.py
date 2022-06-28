#Dictionary Comprehension
#new_dict = {new_key:new_value for item in list}
#이미 존재하는 dictionary에 넣기 - dict의 모든 아이템을 key, value로 나누고 각각을 new_key와 new_value에 저장
#new_dict = {new_key:new_value for (key, value) in dict.item()}


#Conditional Dictionary Comprehension
#new_dict = {new_key:new_value for (key, value) in dict.item() if test}


names = ["Alex" ,"Tim", "Jerry", "Condaniel", "Kims", "Dave"]

import random
students_scores = {student:random.randint(1, 100) for student in names}

print(type(students_scores))
print(students_scores)
# <class 'dict'>
# {'Alex': 4, 'Tim': 7, 'Jerry': 84, 'Condaniel': 43, 'Kims': 36, 'Dave': 36}


passed_students = {student:score for (student, score) in students_scores.items() if score > 40}
print(passed_students)
#{'Alex': 57, 'Tim': 45, 'Dave': 80}
