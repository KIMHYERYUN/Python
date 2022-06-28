#터틀 경쟁
#누가 이길것 같은지 내기를 묻는 팝업창 - 색상
#화면 좌측에 출발위치 정렬 - 오른쪽 가장자리를 향해 달림
#내기에서 이겼는지 졌는지 결과 - 누가 이겼는지
import turtle
from turtle import Turtle, Screen

import random

screen = Screen()

#창의 크기 설정
screen.setup(width=500, height=400)

#팝업창 - 입력받기
user_bat = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? you can choice blue, yellow, red, pink, silver, green. Enter a color: ")

#입력받은 값 - 콘솔창에 출력
print(user_bat)

#경주마 색상 : 경주마 색상 rgb 이용시 다양한 색상이 나타나나, 너무 다양하여 choice하기 어려움
# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
color_list = ["blue", "yellow", "red", "pink", "brown", "silver", "green"]


#경주마 객체 리스트
turtle_list = []

#경주마 객체 생성하기
def make_turtle(turtle_num):
    for i in range(1, turtle_num+1):
        #객체생성
        tim = Turtle()
        #객체모양
        tim.shape("turtle")
        #객체랜덤색상
        #tim.color(random.color())
        #tim.color(random.choice(color_list)) : 오류 - 동일 색상 발생가능
        tim.color(color_list[i-1])
        #객체 들어올리기
        tim.penup()
        #객체 이동
        tim.goto(x=-200, y=-200 + i*50)
        #객체 내리기
        #tim.pendown() - 선이 그어짐
        #만든 객체를 리스트에 추가
        turtle_list.append(tim)


make_turtle(6)

#레이스 시작여부
is_race_on = False
#입력한 경우 레이스 시작
if user_bat:
    is_race_on = True

#레이스 시작
while is_race_on:
    # 랜덤하게 움직이기
    for turtle in turtle_list:
        #마지막 결승선 설정하여 도착시 멈춤 - x좌표 함수(xcor)
        if turtle.xcor() > 200:
            #먼저 도착한 터틀이 있을경우 멈춤
            is_race_on = False
            #print(turtle.color) #두개의 요소 : color(테두리, 페인팅)
            #먼저 도착한 색상 가져오기
            winnig_color = turtle.pencolor()
            #답안이 맞는지 확인
            if winnig_color == user_bat:
                print(f"You've won! The {winnig_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winnig_color} turtle is the winner!")
        # 랜덤하게 앞으로 가는 간격
        turtle.forward(random.randint(1, 10))
        # 랜덤하게 앞으로 가는 스피드(0~10) / fastest = 0, slowest = 1, slow = 3, normal = 6, fast = 10
        turtle.speed(random.randint(0, 11))

screen.exitonclick()

