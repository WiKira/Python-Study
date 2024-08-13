from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 0
        self.next_level()

    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)