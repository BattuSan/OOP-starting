import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

direction = [0, 90, 180, 270]

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

current_speed = 0
thick = 3

for i in range(10000):
    tim.forward(20)
    tim.setheading(random.choice(direction))
    tim.color(random_color())
    tim.speed(current_speed)
    tim.width(thick)
    current_speed += 1
Screen().exitonclick()
