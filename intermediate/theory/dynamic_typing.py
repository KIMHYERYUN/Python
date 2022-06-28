#타이핑 : 데이터 타입 정의 - 동적 vs 정적
#동적타이핑 : 변수 또는 인수를 미리 선언하지 않아도 자동으로 메모리 공간 할당


#데이터 유형을 자유롭게 변형 - 별도의 데이터 유형을 선언하지 않아도 변수가 그 값에 연결
#c : 디버그를 돌리면서 메모리 주소를 알 수 있음
#python : 디버그 과정에서 셀 주소를 알기 힘듦 - 메모리 값이 있은 위치 id 활용

#https://stackoverflow.com/questions/11328920/is-python-strongly-typed

a = 6.19
print(type(a))
print(id(a))
a = 5
print(type(a))
print(id(a))
a = "Hyeryun"
print(type(a))
print(id(a))
a = True
print(type(a))
print(id(a))
a = [1, 2, 3]
print(type(a))
print(id(a))

'''
<class 'float'>
2017276820496
<class 'int'>
2017274784176
<class 'str'>
2017276739632
<class 'bool'>
140714961365096
<class 'list'>
2017276735104
'''

b=6
c=6
print(id(b))
print(id(c))
#2179277154768
#2179277154768

b=7
print(id(b))
#2358949079536

#각 리스트의 주소 값 확인
List1= [1, 2, 3, 4, 5]
print(id(List1))
print(id(List1[0]), id(List1[1]), id(List1[2]), id(List1[3]), id(List1[4]))

List2 = List1
print(id(List2))
print(id(List2[0]), id(List2[1]), id(List2[2]), id(List2[3]), id(List2[4]))

'''
1759900803904
1759898528048 1759898528080 1759898528112 1759898528144 1759898528176
1759900803904
1759898528048 1759898528080 1759898528112 1759898528144 1759898528176
'''
#리스트의 값과 안의 원소가 같은 경우 주소가 같다


#리스트 내의 한개의 값을 바꿀경우
List1[0] = 8
print(id(List1))
print(id(List1[0]), id(List1[1]), id(List1[2]), id(List1[3]), id(List1[4]))
'''
2257546978048
2257541818896 2257541818704 2257541818736 2257541818768 2257541818800
'''
#리스트의 주소는 그대로이며, 바뀐 원소의 주소만 바뀜

#바뀐 후 리스트 2dy개의 동일성
print((List1==List2), (List1 is List2))
#True True



#동일한 원소를 가진 또다른 리스트 생성 시
List3= [8, 2, 3, 4, 5]
print(id(List3))
print(id(List3[0]), id(List3[1]), id(List3[2]), id(List3[3]), id(List3[4]))
'''
2761213985280
2761211669008 2761211668816 2761211668848 2761211668880 2761211668912
'''
#리스트의 주소는 다르나 원소의 주소는 같음


##리스트를 저장하는 메모리가 따로있으며 각 원소를 저장하는 메모리가 개별적으로 분리
#내부의 값이 같으면 원소의 주소는 같으나 리스트 주소는 다름