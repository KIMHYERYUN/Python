#변수(variable) : 자료 일시적 보관 및 처리결과 담는 역할, 실제 값을 저장하는 메모리의 이름
#변수에 저장될 값이 메모리에 객체형태로 저장 - 객체의 주소가 변수에 저장 -> 실제값이 저장된 주소를 기억하는 참조형 변수
#변수명의 규칙
#파악하기 쉬운 이름, 첫자 영문자, 공백 및 특수문자 사용불가, 예약어 x, 두번째 단어는 숫자와 _ 사용가능, 대소문자 구분,
#두개의 단어로 이루어진 변수명 사용시 두번째 단어의 첫자는 대문자로 표기

var1 = "Hello Hyeryun"
print(var1)
print(id(var1))
var2 = 900619
print(var2)
print(id(var2))
var3 = True
print(var3)
print(id(var3))
#각 변수에 해당하는 id 다르게 배치

var3 = False
print(var3)
print(id(var3))
#기존 변수에 다른 값으로 수정 시 id도 변함 - 새로운 객체 생성