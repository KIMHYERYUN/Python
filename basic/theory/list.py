#list = [item1, item2, item3.....]
#대괄호 사용
#숫자, 문자, boolean 등 사용가능

#리스트 순서가 있음  : 저장된 순서 - index 활용

list = [3, "0", "ABC", True]
print(list[0])
print(list[1])
print(list[2])
print(list[3])

#다양한 데이터 타입 삽입가능

#list 내의 요소 수정가능
list[2] = "Hello"
print(list)

#list의 function
#append(1개 항목), extend(각철자/리스트 내의 항목을 삽입할 항목), insert(추가할 자리 index, 추가항목)
#remove(제거할항목), pop([인덱스, 인덱스를 안쓸경우 마지막 제거])
#sort(기본값 : 오름차순, reverse=True : 내림차순, key=함수 : 함수에 적용된 결과에 따라 정렬 ex) key = len(길이))

#append : 항목 추가
list.append("추가된요소")
print(list)
#[3, '0', 'Hello', True, '추가된요소']

#extend : 확장(항목 - 단어철자, 리스트 - 각 항목)
list.extend("WHO")
print(list)
#[3, '0', 'Hello', True, '추가된요소', 'W', 'H', 'O']
list.extend(["AM", "I"])
print(list)
#[3, '0', 'Hello', True, '추가된요소', 'W', 'H', 'O', 'AM', 'I']

#insert : 원하는 자리에 항목 추가
#첫번째 자리에 추가
list.insert(0, "First")
print(list)
#['First', 3, '0', 'Hello', True, '추가된요소', 'W', 'H', 'O', 'AM', 'I']

#remove : 제거
list.remove("First")
print(list)
#[3, '0', 'Hello', True, '추가된요소', 'W', 'H', 'O', 'AM', 'I']

#pop : 해당 index 항목 제거
#첫번째 요소 제거
list.pop(0)
print(list)
#['0', 'Hello', True, '추가된요소', 'W', 'H', 'O', 'AM', 'I']

#index 구하기
list.index("찾을내용")

