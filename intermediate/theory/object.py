#another_module.py에서의 변수 가져오기

import another_module

print(another_module.another_variable)
#10



#새로운 객체 형성

#turtle 모듈 가져오기
##https://docs.python.org/3/library/turtle.html
import turtle
#turtle이라는 모듈에 있는 Turtle이라는 클래스 불러오기
#timmy라는 객체 생성
timmy = turtle.Turtle()

#위를 한줄로 나타내기
from turtle import Turtle
timmy = Turtle()
print(timmy)

#모양 및 색깔 바꾸기 - 함수이용
timmy.shape("turtle")
timmy.color("coral")
#모양 앞으로 걸음 걸어가기 - 함수이용
timmy.forward(100)

#<turtle.Turtle object at 0x0000024436027460>
#위 주소에 저장된 객체

#class.object.attribute
#클래스 - 객체 - 속성
#class.object.method
#클래스 - 객체 - 함수

#Screen이라는 객체를 생성하여 그 안의 속성을 출력
from turtle import Screen
#Screen의 객체 생성
my_screen = Screen()
#Screen의 새로운 객체인 my_screen에서의 canvheight속성 가져오기
print(my_screen.canvheight)

#Screen이라는 객체를 생성하여 그 안의 함수를 활용
#위 코드까지는 스크린이 나타났다가 코드가 종료될시 자동 사라졌으나,
#스크린을 클릭해야만 스크린이 사라지는 함수 - 함수이용
my_screen.exitonclick()


