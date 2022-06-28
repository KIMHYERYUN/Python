import turtle as t
import random

tim = t.Turtle()
tim.shape("arrow")

colors = ["green", "blue", "deep pink", "purple", "gold", "deep sky blue", "silver", "black", "dark cyan"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for num_sides in range(3, 11):
    random_color = random.choice(colors)
    tim.color(random_color)
    draw_shape(num_sides)


screen = t.Screen()
screen.exitonclick()