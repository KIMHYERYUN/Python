#리스트나 튜플의 일부부을 가져오기
#방법1. 각 하나씩 추출하여 빈공간에 추가하기
#방법2. slicing

#slicing
#가져올 변수명[첫번째 index : 마지막 index : 증가분 숫자+1]
#첫번째부터 마지막 -1까지 원소 추출
#생략시 처음이나 마지막 다 가져오기


#인덱스는 해당 요소의 바로 앞에 붙어진 이름이라 생각
#index 0 - 첫번째 / index 1 - 두번째 / 등등

#리스트
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[:]) #전체
print(piano_keys[1:5]) #b,c,d,e
print(piano_keys[:3])  #a,b,c
print(piano_keys[2:])  #c,d,e,f,g
print(piano_keys[::2]) #한개씩 건너서 추출, a,c,e,g
print(piano_keys[::-1]) #역순으로 추출, g,f,e,d,c,b,a
print(piano_keys[::-2]) #역순 한개씩 건너서 추출, g,e,c,a

['a', 'b', 'c', 'd', 'e', 'f', 'g']
['b', 'c', 'd', 'e']
['a', 'b', 'c']
['c', 'd', 'e', 'f', 'g']
['a', 'c', 'e', 'g']
['g', 'f', 'e', 'd', 'c', 'b', 'a']


#튜플
piano_tuple = ["do", "re", "mi", "fa", "sol", "ra", "si"]
print(piano_tuple[:]) #전체
print(piano_tuple[1:5]) #re,mi,fa,sol
print(piano_tuple[:3])  #do,re,mi
print(piano_tuple[2:])  #mi,fa,sol,ra,si
print(piano_tuple[::2]) #한개씩 건너서 추출, do,mi,sol,si
print(piano_tuple[::-1]) #역순으로 추출, si,ra,sol,fa,mi,re,do
print(piano_tuple[::-2]) #역순 한개씩 건너서 추출, si, sol, mi, do

['do', 're', 'mi', 'fa', 'sol', 'ra', 'si']
['re', 'mi', 'fa', 'sol']
['do', 're', 'mi']
['mi', 'fa', 'sol', 'ra', 'si']
['do', 'mi', 'sol', 'si']
['si', 'ra', 'sol', 'fa', 'mi', 're', 'do']
['si', 'sol', 'mi', 'do']
