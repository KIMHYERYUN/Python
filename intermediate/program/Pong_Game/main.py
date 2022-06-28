from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

#화면구성
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Kim's Pong game!")
#패들이 이동하는 애니메이션 off
screen.tracer(0)


#패들구성
paddle_user = Paddle((-350, 0))
paddle_com = Paddle((350, 0))

#볼 구성
ball = Ball()

#점수판 구성
score_board = Scoreboard()

#각 패들 조작
screen.listen()
screen.onkey(paddle_user.go_up, "w")
screen.onkey(paddle_user.go_down, "s")
screen.onkey(paddle_com.go_up, "Up")
screen.onkey(paddle_com.go_down, "Down")


is_game_on = True


while is_game_on:
    # 공의 속도 증가
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # 공이 벽에 닿는 경우
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # 공이 패들에 닿는 경우
    if ball.distance(paddle_com) < 50 and ball.xcor() > 340 or ball.distance(paddle_user) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()

    # 공이 패들을 놓칠 경우 - 볼 리셋 -  - 점수 증가
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.user_add_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.com_add_score()

screen.exitonclick()