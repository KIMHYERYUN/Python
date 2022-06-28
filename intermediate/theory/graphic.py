#turtle 모듈에서 Turtle, Screen 클래스 가져오기
from turtle import Turtle, Screen

#창 나왔다가 사라짐
timmy_the_turtle = Turtle()

#모양 바꾸기
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
#tk=tkinter 모듈 : 그래픽 모듈
#파이썬을 이용해 GUI(Graphic User Interface)라 불리는 그래필 사용자 인터페이스를 생성하기 위한 수단 중 하나
#텍스트 인터페이스 - 텍스트, 그래픽 인터페이스 - 이미지 표시, 클릭과 드래그를 통해 눈으로 보면서 작업수행

#움직이기
#앞으로 나가기
timmy_the_turtle.forward(100)
#오른쪽으로 돌기
timmy_the_turtle.right(90)









#스크린을 불러 창을 유지시키기 - 클릭 한번
screen = Screen()
screen.exitonclick()