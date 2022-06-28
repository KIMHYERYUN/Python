#사용자의 입력을 듣고 실행하는 함수

from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


#스페이스바를 누르면 앞으로 전진
screen.listen()
screen.onkey(key="space", fun=move_forward)
#space바 키를 누를때 move_forward라는 함수가 실행되는 것
#move_forward() 괄호를 붙이게 되면 바로 실행되므로 생략
screen.exitonclick()


