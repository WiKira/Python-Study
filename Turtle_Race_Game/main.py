from turtle import Turtle, Screen
from random import randint, choice

is_race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

y = -150
turtles = []
for _ in range(7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[_])
    new_turtle.up()
    new_turtle.goto(-230, y)
    turtles.append(new_turtle)
    y += 50

if bet:
    is_race_on = True

winner_color = ""

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            is_race_on = False
            break
        random_dist = randint(0, 10)
        turtle.forward(random_dist)

screen.bye()

if bet == winner_color:
    print(f"Winner winner chicken dinner, you was right, the {winner_color} turtle is the winner.")
else:
    print(f"Loserrrrrr, the real winner is {winner_color}.")

# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def reset_game():
#     tim.home()
#     tim.clear()
#
#
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=turn_left)
# screen.onkeypress(key="d", fun=turn_right)
# screen.onkeypress(key="c", fun=reset_game)
#
# screen.listen()
screen.exitonclick()
