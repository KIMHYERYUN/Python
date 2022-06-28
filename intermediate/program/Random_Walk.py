#도박꾼의 재정상태, 액체기체 포함된 분자경로, 먹이탐색 동물경로 등 모델링
#방향 임의
#움직일때마다 다른 색상
#선의 굵기
#스크린사이즈 - 가로 50%, 세로 75% 권고 (직접 크기를 설정, 또는 퍼센트)

import turtle as t
import random

#영역크기 설정
t.setup(500, 500)

tim = t.Turtle()

#모양 바꾸기
tim.shape("circle")

#굵기 바꾸기
tim.pensize(20)
#속도 바꾸기
tim.speed("fastest")

#각도와 색상 선택지
angles = [90, 180, 270, 360]
#colorstring 이용
colors = ["green", "blue", "deep pink", "purple", "gold", "deep sky blue", "silver", "black", "dark cyan"]
#color rgb 이용
#colormode = 1.0 에서 255 숫자
#rgb calculator
#색상모드 설정 - 255까지
colors_rgb = t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


#임의의 방향과 선 그리기
def draw_shape():
    random_angle = random.choice(angles)
    #random_color = random.choice(colors)
    tim.right(random_angle)
    #tim.color(random_color)
    tim.color(random_color())
    tim.forward(50)

#200개 그리기
for num in range(200):
    draw_shape()


screen = t.Screen()
#스크린 사이즈 바꾸기
screen.screensize(500, 500)
screen.exitonclick()
