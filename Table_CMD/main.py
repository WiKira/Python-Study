#import time
#from turtle import Turtle, Screen
#
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("cyan")
#
#for i in range(0, 50):
#    timmy.forward(2)
#
#    if i % 10 == 0:
#        time.sleep(0.5)
#
#
#my_screen = Screen()
#
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon", "Type"]

table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

table.add_column("Size", ["100", "80", "120"])

table.align = "l"

table.align["Size"] = 'r'


print(table)