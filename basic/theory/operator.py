#연산자(operator) : 연산기호와 기능
#산술연산자, 관계연산자, 논리연산자, 대입연산자
#산술연산자 : 사칙연산, 나머지 및 몫 반환, 지수 등
#관계연산자 : 동등비교, 크기비교
#논리연산자 : 논리곱, 논리합, 부정
#대입연산자 : 같다, 교환, 패킹(묶어서 할당)

#산술연산자
num1 = 100
num2 = 200

add = num1 + num2
print(add)
sub = num1 - num2
print(sub)
mul = num1 * num2
print(mul)
div = num2 / num1
print(div)
div2 = num2 % num1
print(div2)
square = num1**2
print(square)

#정수/정수, 정수/실수, 실수/정수 -> 실수
print(type(10/2))
print(type(10/1.5))
print(type(12.5/5))
print(type(12.5/1.5))

#round : 반올림, round(대상, n번째 자리에서 반올림)
#// : 버림 => 정수

# a += b : a = a + b의 줄임말
# a -= b : a = a - b의 줄임말


#관계연산자
#논리연산자(logical operator)
# A and B : 둘다 참
# C or D : 둘 중 하나 참
# not E : 아닌, 역

#대입연산자



#비교연산자(Comparison Operator)
# >(크다), <(작다), >=(크거나 같다), <=(작거나 같다), ==(같다), !=(같지않다)

#=, ==의 차이점 : 지정과 같은지 확인
# = : 값을 변수로 지정해준다는 의미
# == : 왼쪽의 값이 오른쪽의 값과 같은지 확인 - 결과값이 boolean
