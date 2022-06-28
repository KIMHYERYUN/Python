from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Kim's snake game")

#뱀 생성
snake = Turtle(shape="square")   #사각형모양
snake.color("white")   #하얀색
snake.shapesize(stretch_wid=0.5, stretch_len=1.5)   #폭 0.5, 길이 1.5
print(snake.position()) #위치 확인 - (0.00,0.00)
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
#starting_position = [(0,0), (-20,0), (-40,0)]
#segments = []
#for position in starting_positions:
#   new_segment = Turtle("square")
#   new_segment.color("white")
#   new_segment.goto(position)
#   segments.append(new_segment)

#게임진행여부
is_game_on = True
while is_game_on:
    snake.forward()


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
#사각형을 합쳤을경우
#화면 바뀔때마다의 애니매이션이 보여지는 것을 off -update 될때까지
#screen.tracer(0)
#screen.update()












screen.exitonclick()