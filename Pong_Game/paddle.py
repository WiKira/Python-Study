from turtle import Turtle

START_POSITIONS = [(-350, 0), (350, 0)]


class Paddle(Turtle):

    def __init__(self, player_num):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.goto(START_POSITIONS[player_num-1])
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        y_pos = self.ycor() + 70 if self.ycor() + 70 < 250 else 250
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos = self.ycor() - 70 if self.ycor() - 70 > -250 else -250
        self.goto(self.xcor(), y_pos)
