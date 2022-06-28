from turtle import Turtle, Screen

#Turtle 객체 생성
timmy_the_turtle = Turtle()
#화살표 모양으로 바꾸기
timmy_the_turtle.shape("arrow")

#전진
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

for i in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()