from turtle import Turtle, Screen
import random


def position(t_list):
    ref_local = -50
    for i in t_list:
        i.penup()
        i.setposition(-230, ref_local)
        ref_local += 50
    return t_list


def final_line():
    f_line = Turtle()
    f_line.ht()
    f_line.penup()
    f_line.setposition(230, 180)
    f_line.pendown()
    f_line.right(90)
    f_line.forward(250)


game_is_on = True

colors = ["red", "green", "blue", "yellow", "purple"]

screen = Screen()
screen.setup(height=400, width=500)
turtles = [Turtle() for i in range(len(colors))]
ref = 0

for t in turtles:
    t.shape("turtle")
    t.color(colors[ref])
    ref += 1

turtles = position(turtles)
final_line()
user_input = screen.textinput(title="Welcome to the game", prompt="Enter the winner by color:")

if user_input:
    while game_is_on:
        for i, all_turtles in enumerate(turtles):
            all_turtles.forward(random.randint(0, 10))
            if all_turtles.xcor() >= 210:
                winner = colors[i]
                game_is_on = False

print(f"The winner is {winner}")

if user_input.lower() == winner.lower():
    print("You win")
else:
    print("You lose")
