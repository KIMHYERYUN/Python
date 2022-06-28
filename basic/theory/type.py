#자료형(type) : 자료의 유형
#별도의 선언 불필요

#숫자형, 문자형, 논리형
#숫자형 : 정수(Integer), 실수(Float) - 통계처리, 차트 등
#문자형(String) : 문자, 문자열 - 자연어 처리 등
#논리형(Boolean) : 참, 거짓 - 조건식 등



#자료형 결합 - 동일 자료형만 가능
#문자 결합
print("abc" + "def")
print("123" + "456")
#숫자 결합
print(123 + 456)
#Large Integer : 큰 숫자 ,단위 = _단위
#123456789 = 123_456_789
print(123456789)
print(123_456_789)
#숫자 + 문자 결합 시 에러
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(6+"19")

#단, f-String 활용시 다른 유형의 데이터 별도의 변환없이 결합 가능 : f, {} 사용
score = 0
height = 168
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

print()


#자료형 확인 함수 : type
var1 = "Hyeryun"
print(var1)
print(type(var1))
var2 = 900619
print(var2)
print(type(var2))
var3 = "900619"
print(var3)
print(type(var3))
var4 = 166.5
print(var4)
print(type(var4))
var5 = True
print(var5)
print(type(var5))

print()



#자료형 변환(type conversion, type casting)
#실수 -> 정수
a = int(166.5)
print(a)
print(type(a))
#정수 -> 실수
b = float(6)
print(b)
print(type(b))
#정수 -> 문자형
c = 19
print(str(c))
print(type(str(c)))
#문자형 -> 정수
d = "19"
print(int(d))
print(type(int(d)))
#논리형 -> 정수
print(int(True))
print(int(False))
