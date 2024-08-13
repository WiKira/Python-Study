from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
tim.shape("turtle")
tim.color("NavyBlue")

# for i in range(4):
#     tim.forward(100)

#     tim.right(90)


# for _ in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

screen = Screen()
screen.colormode(255)

# for _ in range(3, 11):
#     angle = 360/_
#
#     tim.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#     for i in range(_):
#         tim.right(angle)
#         tim.forward(100)
# tim.pensize(10)
tim.speed("fastest")
steps = 100

# for i in range(steps):
#     tim.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
#     res = choice([-1, 0, 1])
#     if res == -1:
#         tim.left(90)
#     elif res == 1:
#         tim.right(90)
#     tim.forward(50)

# directions = [0, 90, 180, 270]
#
#
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple
#
#
# for _ in range(steps):
#     tim.pencolor(random_color())
#     tim.forward(50)
#     tim.setheading(choice(directions))
angle = 5
steps = 360//angle

for _ in range(steps):
    tim.color(random_color())
    tim.circle(100)
    tim.left(angle)

screen.exitonclick()
