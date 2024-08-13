from turtle import  Turtle, Screen
from random import choice
import colorgram

colors = colorgram.extract('image.jpg', 30)

list_tuples = []
for color in colors:
    list_tuples.append((color.rgb.r, color.rgb.g, color.rgb.b))


list_tuples = list_tuples[4:]

print(list_tuples)

screen = Screen()
screen.colormode(255)

tim = Turtle()

x = -250
y = -250

tim.up()
tim.hideturtle()

tim.setposition(x, y)
tim.speed("fastest")


for r in range(10):
    for c in range(10):
        tim.dot(20, choice(list_tuples))
        tim.fd(70)
    y += 70
    tim.setposition(x, y)


screen.exitonclick()
