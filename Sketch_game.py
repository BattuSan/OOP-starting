from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def front():
    tim.forward(10)


def back():
    tim.backward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


tim.speed("fastest")
screen.listen()
screen.onkey(key="w", fun=front)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.exitonclick()
