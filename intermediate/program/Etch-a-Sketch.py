#w-Forwards
#s-Backwards
#a-Counter-Clockwise
#d-Clockwise
#c-Clear drawing

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_counter_clockwise():
    tim.left(10)
    #new_heading = tim.heading() + 10
    #tim.setheading(new_heading)
def move_clockwise():
    tim.right(10)
def clear_drawing():
    tim.clear()
    #원위치
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
#screen.onkey(move_forward, "w")
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

#오류 : fun 부분에 ""가 아님