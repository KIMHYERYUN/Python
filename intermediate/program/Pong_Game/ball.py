from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1)
        self.goto(0, 0)
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.02

    #공이 움직이는 함수 - 지속적을 10씩 증가
    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    #공이 벽에 부딪히면 y좌표가 반대방향으로 작용
    def bounce_wall(self):
        self.y_move *= -1
        #속도가 증가하기 위해 숫자 줄어들어야 함
        self.move_speed *= 0.9

    #공이 패들에 부딪히면 x좌표가 반대방향으로 작용 - 스피드 증가
    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 1.5

    #공의 위치가 리셋
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.02
        self.bounce_paddle()