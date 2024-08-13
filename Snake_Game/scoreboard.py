import os.path
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 250)
        self.display_score()
        self.get_highscore()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.home()
    #     self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)
    def get_highscore(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt") as file:
                self.highscore = int(file.read())
