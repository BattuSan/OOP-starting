from turtle import Turtle, Screen

jim = Turtle()
degree = 0
jim.speed(10)
while degree < 360:
    jim.circle(100)
    jim.setheading(degree)
    degree += 5

Screen().exitonclick()
