from turtle import Turtle, Screen
#위에 Turtle이라는 클래스 미사용 : 이유는 아래 클래스에서 종속되어 이미 사용되었기 때문에
from snake_sumsquare import Snake_sumsquare
from foody_sumsqare import Food_sumsquare
from scoreboard_sumsquare import Scoreboard_sumsquare

import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Kim's snake game")
#애니매이션 끄기 - 이동간의 흐름 보지않기(update 나올때까지)
#사각형을 합쳤을경우
#화면 바뀔때마다의 애니매이션이 보여지는 것을 off -update 될때까지
screen.tracer(0)


#객체 형성
#뱀 객체
snake = Snake_sumsquare()
#아이템 객체
food = Food_sumsquare()
#점수판 객체
scoreboard = Scoreboard_sumsquare()

#조작법 설정 - 오류 : key = "파스칼표기" / up(x), Up(o)
screen.listen()
screen.onkey(key="Up", fun=snake.go_up)
screen.onkey(key="Down", fun=snake.go_down)
screen.onkey(key="Left", fun=snake.go_left)
screen.onkey(key="Right", fun=snake.go_right)

#게임진행여부
is_game_on = True
while is_game_on:
    #움직이고 나서 update하면 갱신된 화면만 보임
    screen.update()
    # 1초씩 지연 : 숫자가 작아질수로고 빨라짐
    time.sleep(0.1)

    snake.movesnake()

    #아이템을 먹을경우(turtle.distance(비교대상))
    if snake.head.distance(food) < 15: #아이템의 크기고려하여 그 간의 거리 지정
        print("nom nom nom") #콘솔에 표시
        #아이템 사라지고 재생성
        food.refresh()
        #점수 증가
        scoreboard.increase_score()
        #뱀 꼬리 스퀘어 하나 증가
        snake.extendsegment()


    #벽에 부딪힐 경우 - 경계선 x축, y축 -230 ~ 230
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() < -230 or snake.head.ycor() > 230:
        is_game_on = False
        scoreboard.game_over()

    #뱀의 머리가 자신의 몸통과 부딪힐 경우 - 머리와 각 몸통의 거리로 판단 (단, 자신의 몸통이 머리일 경우 제외)
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         scoreboard.game_over()
    #슬라이싱 이용하기
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()