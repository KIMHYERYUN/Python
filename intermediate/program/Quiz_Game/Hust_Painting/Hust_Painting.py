#중심점 아래 이동
#왼쪽방향으로 간격 뛰면서 점을 찍음
#랜덤 색상
#20개씩찍고 위로 올라가서 찍기

import random
import turtle as t
tim = t.Turtle()

#현재위치 확인
(tim.position())

#시작위치 설정
#오류 : 이동시 선이 그어짐
tim.penup()
tim.goto(-300, -300)

#색상
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#간격, 가로로 그리고 싶은 갯수, 새로로 그리고 싶은 갯수를 변수로 집어넣은 그리는 함수
def draw_dot(gap, x_num, y_num):
    for i in range(1, y_num+1):
        #가로에 찍고 싶은 숫자
        for _ in range(x_num):
            #점찍기 - 점크기 10
            tim.dot(10, random_color())
            #이동하기
            tim.penup()
            tim.forward(gap)
        tim.goto(-300, -300 + i * gap)


draw_dot(50, 10, 10)

screen = t.Screen()
screen.exitonclick()