from turtle import Turtle
import random
#터틀 클래스가 할 수 있는 모든일을 할수있게 상속
class Food_sumsquare(Turtle):

    def __init__(self):
        #상위 클래스의 init 함수 삽입
        super().__init__()
        #turtle 클래스가 가진 함수 사용가능
        self.shape("circle") #아이템 모양
        #이동하는 부분 제거
        self.penup() #펜들기
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  #기본 20*20 - 10*10으로 수정
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    #아이템 랜덤하게 발생
    def refresh(self):
        self.goto(random.randint(-220, 220), random.randint(-220, 220)) #랜덤위치 선정 - 뱀이 먹을수있는 위치 선정
