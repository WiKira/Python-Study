from turtle import Turtle

FONT = ("Courier", 100, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pensize(5)
        self.pencolor("white")
        self.player_1_score = 0
        self.player_2_score = 0
        self.draw_table()

    def draw_screen(self):
        self.clear()
        self.draw_table()
        self.update_score()

    def draw_table(self):
        self.goto(0, 300)
        self.setheading(270)

        while self.ycor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def update_score(self):
        self.penup()
        self.goto(-100, 150)
        self.write(self.player_1_score, move=False, align="center", font=FONT)
        self.goto(100, 150)
        self.write(self.player_2_score, move=False, align="center", font=FONT)

    def make_point(self, ball_position):
        if ball_position < -380:
            self.player_2_score += 1
        else:
            self.player_1_score += 1

        self.draw_screen()
