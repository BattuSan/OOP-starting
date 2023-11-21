import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
real_angle = 90
sides = 4
size = 20
while sides <= 20:
    for _ in range(sides):
        timmy.forward(size)
        timmy.right(real_angle)
    sides += 1
    real_angle = 360 / sides
    size += 10

Screen().exitonclick()
