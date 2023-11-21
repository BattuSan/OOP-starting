import turtle
from turtle import Turtle, Screen
import colorgram
import random

turtle.colormode(255)
colors = colorgram.extract("spot_paintings.jpg",25)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

tim = Turtle()
tim.penup()
for position in range(5):
    tim.setposition(0,(position+1)*50)
    for i in range(5):
        tim.forward(100)
        tim.dot(20, random.choice(color_list))
Screen().exitonclick()
