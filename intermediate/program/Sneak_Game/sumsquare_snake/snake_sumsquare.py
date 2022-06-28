#뱀과 관련된 것

from turtle import Turtle
import time

#시작위치 - 상수이름은 모두 대문자
#한곳에 변경하기 쉽게 모여둠
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake_sumsquare:
    def __init__(self):
        self.segments = []
        self.createsnake()
        #뱀의 움직임은 머리가 움직이면 따라움직이므로 머리설정
        self.head = self.segments[0]

    #뱀의 객체생성
    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)

    #뱀 꼬리 생성
    def addsegment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    #뱀 꼬리 증가
    def extendsegment(self):
        #마지막 꼬리의 위치에 추가
        self.addsegment(self.segments[-1].position())


    def movesnake(self):
        # 뱀의 이동시 모양
        # segment_1 - 이동, segment_2 = segment_1 위치, segment_3 = segment_2 위치
        # for seg_num in range(start=2 , stop=0, step=-1): #2-1-0, TypeError: range() takes no keyword arguments
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # 첫번째 segment 이동
        self.head.forward(MOVE_DISTANCE)


    #뱀의 조작법
    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def go_left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)
    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

