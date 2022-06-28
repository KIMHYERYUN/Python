from turtle import Turtle, Screen
ALIGN = "center"
FONT = ("Arial", 8, "normal")

class Scoreboard_sumsquare(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  #초기 점수 설정
        #높은 점수 관리 데이터 연결
        with open("high_score_data.txt") as data:
            self.highscore = int(data.read())
        self.highscore = 0 #높은 점수 설정
        self.penup() #펜 올리기
        self.goto(0, 230) #상단에 배치, 점수를 쓰기전에 배치
        self.color("white") #색깔변경
        #새로운 객체 turtle을 제거(숨기기)
        self.hideturtle()
        #점수 업데이트
        self.update_score()

    #점수판 업데이트
    def update_score(self):
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGN, font=FONT)  # 점수판 설정 - 현재, 최고점수

    #점수 업데이트
    def increase_score(self):
        self.score += 1
        #이전 점수 지우기
        self.clear()
        self.update_score()


    #게임 종료
    def game_over(self):
        #정중앙으로 옮겨서 문구 출력
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)

    #최고점수 업데이트
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            #데이터 파일을 열어 작성
            with open("high_score_data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        #현재 점수는 리셋
        self.score = 0
        self.update_score()