#원 반지름 100
#동작 끝
import random
import turtle as t

tim = t.Turtle()

#속도 조절
tim.speed("fastest")

#색상
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#원위치
tim.home()
#위치확인
print(tim.position())  # 0.0

#오류 : 그렸던 원에 겹쳐서 그려짐 - 원의 간격을 활용
#원의 간격만큼 중심을 이동, 간격만큼 그리기
def draw_circle(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        # 랜덤색상선택
        tim.color(random_color())
        #원그리기 - 반지름 100
        tim.circle(100)
        #방향바꾸기
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

#draw_circle(5)
#오류 : float - int ; for i in range(int(360 / size_of_gap)):
draw_circle(10)
draw_circle(100)

screen = t.Screen()
screen.exitonclick()