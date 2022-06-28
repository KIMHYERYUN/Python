from turtle import Turtle

STARTING_POSITION = (0, -250)

class TurtleManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        #모양
        self.shape("turtle")
        #색상
        self.color("black")
        #들어올려서 위치
        self.penup()
        self.setposition(STARTING_POSITION)
        #방향
        self.setheading(90)

    # 조작법
    def go_up(self):
        self.forward(10)


    #성공여부
    def success_check(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    #처음으로 돌아가기
    def goto_start(self):
        self.goto(STARTING_POSITION)