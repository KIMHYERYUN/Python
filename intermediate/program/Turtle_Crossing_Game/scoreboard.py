from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-250, 250)
        self.update_score()

    #레벨 업데이트
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    #레벨 증가
    def increase_level(self):
        self.level += 1
        self.update_score()

    #레벨 종료
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
