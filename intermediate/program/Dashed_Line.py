from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")

for i in range(15):
    timmy_the_turtle.forward(10) #10걸음 앞으로 나아가기
    timmy_the_turtle.penup() #펜을 들어올리고
    timmy_the_turtle.forward(10) #10걸음 앞으로 나아가기 - 빈칸
    timmy_the_turtle.pendown() #펜을 내려놓고


screen = Screen()
screen.exitonclick()