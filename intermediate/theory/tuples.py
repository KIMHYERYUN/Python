#tuple = ( , )
#list = [ , ]

#공통점
#index 활용하여 요소를 출력할 수 있음

#차이점
#tuple : 리스트처럼 값 변경이 어려움, 돌에 새겨있는 것처럼 = immutable
#일정하게 변하지 않고자 하는 리스트들을 표현
#리스트로 변환도 가능 : list(tuple)

my_tuple = (1, 4, 10)
my_list = [1, 4, 10]

print(my_tuple[0])   #1
print(my_list[0])    #1

#my_tuple[0] = 5     #TypeError: 'tuple' object does not support item assignment
print(my_tuple[0])  #1, 변하지 않음
my_list[0] = 5
print(my_list[0])   #5

print(my_tuple)
print(my_list)

# (1, 4, 10)
# [5, 4, 10]


