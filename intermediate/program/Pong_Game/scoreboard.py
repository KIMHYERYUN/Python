from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        #turtle보다 입력에 대한 부분이 중요하므로 turtle 숨김
        self.hideturtle()
        self.user_score = 0
        self.com_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"Player1 : {self.user_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(200, 200)
        self.write(f"Player2 : {self.com_score}", align="center", font=("Courier", 20, "normal"))

    def user_add_score(self):
        self.user_score += 1
        self.update_score()

    def com_add_score(self):
        self.com_score += 1
        self.update_score()