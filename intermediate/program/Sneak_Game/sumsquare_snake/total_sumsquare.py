from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Kim's snake game")
#애니매이션 끄기 - 이동간의 흐름 보지않기(update 나올때까지)
#사각형을 합쳤을경우
#화면 바뀔때마다의 애니매이션이 보여지는 것을 off -update 될때까지
screen.tracer(0)
#뱀 생성
snake = Turtle(shape="square")   #사각형모양
snake.color("white")   #하얀색
#사각형 3개를 만들어 이어붙어도 가능
#segment_1 = Turtle("square")
#segment_1.color("white")
#segment_2 = Turtle("square")
#segment_2.color("white")
#segment_2.goto(-20,0)
#segment_3 = Turtle("square")
#segment_3.color("white")
#segment_3.goto(-40,0)
#방법2
starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []
for position in starting_positions:
   new_segment = Turtle("square")
   new_segment.color("white")
   new_segment.goto(position)
   segments.append(new_segment)


import time
#게임진행여부
is_game_on = True
while is_game_on:
    #움직이고 나서 update하면 갱신된 화면만 보임
    screen.update()
    # 1초씩 지연 : 숫자가 작아질수로고 빨라짐
    time.sleep(0.1)
    #뱀의 이동시 모양
    #segment_1 - 이동, segment_2 = segment_1 위치, segment_3 = segment_2 위치
    #for seg_num in range(start=2 , stop=0, step=-1): #2-1-0, TypeError: range() takes no keyword arguments
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    #첫번째 segment 이동
    segments[0].forward(10)


#뱀의 조작법
def go_up():
    snake.setheading(90)
    snake.forward(10)
def go_down():
    snake.setheading(270)
    snake.forward(10)
def go_left():
    snake.left()
    snake.forward(10)
def go_right():
    snake.right()
    snake.forward(10)
screen.onkey(key="up", fun=snake.go_up)
screen.onkey(key="down", fun=snake.go_down)
screen.onkey(key="left", fun=snake.go_left)
screen.onkey(key="right", fun=snake.go_right)














screen.exitonclick()