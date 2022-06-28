#import 모듈명
#자세한 내용은 : goto > implementation

#from 모듈명 import 모듈내의 클래스명
#모듈명.클래스명

from turtle import Turtle
a = Turtle()
b = Turtle()
c = Turtle()

#a = trutle.Turtle()
#b = trutle.Turtle()
#c = trutle.Turtle()


#from 모듈명 import * : 모든 클래스와 상수 삽입
#단, 코드실행에 이상은 없으나 어디서 부터 온것인지 알수가 없음
#단, messagebox 같은 별도의 모듈이나 코드가 존재할 경우 *에 포함되지 않을 수 있으니 유의

#import 모듈명 as 명칭(alias name)
import turtle as t
a = t()
b = t()
c = t()


#표준 라이브러리 외의 라이브러리는 설치필요
import heroes
print(heroes.gen())
