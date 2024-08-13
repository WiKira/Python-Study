import turtle
import pandas as pd
from turtle import Screen, Turtle

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()

df = pd.read_csv("50_states.csv")

remain_states = df["state"].tolist()

points = 0

while points < 50:
    guess = turtle.textinput(f"{points}/50 States Correct", "What's another state name?").title()

    if guess == "Exit":
        break
    if guess in remain_states:
        row = df[df["state"] == guess]
        scoreboard.goto(int(row.iloc[0, 1]), int(row.iloc[0, 2]))
        scoreboard.write(guess, move=False, align="center", font=("Arial", 12, "normal"))
        points += 1


if points == 50:
    scoreboard.home()
    scoreboard.write("Congrats, you finish the game", move=False, align="center", font=("Arial", 40, "bold"))
else:
    df_remain = pd.DataFrame(remain_states)
    df_remain.to_csv("remain_stats.csv")

screen.exitonclick()
