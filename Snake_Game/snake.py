from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def grow_segments(self, last_x_position, last_y_position):
        snake = Turtle()
        snake.up()
        snake.color("white")
        snake.shape("square")
        snake.setposition(x=last_x_position - 20, y=last_y_position)
        self.segments.append(snake)
        self.tail = snake

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].position())

        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for _ in range(3):
            last_x = self.segments[len(self.segments) - 1].position()[0] if len(self.segments) > 0 else 20
            self.grow_segments(last_x_position=last_x, last_y_position=0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def touching_tail(self):
        pass

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
            del segment

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]