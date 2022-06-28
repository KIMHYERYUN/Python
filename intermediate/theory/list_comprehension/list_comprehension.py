#List Comprehension
#new_list = [new_item for item in list]

#Conditional List Comprehension
#new_list = [new_item for item in list if test]



#python sequences : list, range, string, tuple : 순서를 가지고 있음
#순서대로 통과
#comprehension 적용가능

numbers = [1, 2, 3]
new_list = []
for n in numbers :
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)
#[2, 3, 4]


new_list_comprehension = [n+1 for n in numbers]
print(new_list_comprehension)
#[2, 3, 4]


name = "Kim"
new_list_name = [letter for letter in name]
print(new_list_name)
#['K', 'i', 'm']

range(1, 5)
new_range = [2*n for n in range(1, 5)]
print(new_range)
#[2, 4, 6, 8]


names = ["Alex", "Beth", "Caroline", "Dave"]
# 5글자 안넘는 조건의 이름 리스트 만들기
short_names = [name for name in names if len(name) < 5]
print(short_names)
#['Alex', 'Beth', 'Dave']

#5글자 이상의 이름은 대문자로 만들기
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
#['CAROLINE']


#짝수 선별
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]