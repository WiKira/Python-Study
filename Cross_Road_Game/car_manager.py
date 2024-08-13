from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_CARS_IN_SCREEN = 50


class CarManager(Turtle):

    def __init__(self):
        self.car_list = []
        self.carsVelocity = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if random.randint(1, 6) == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_cars(self, player):
        for car in self.car_list:
            car.backward(self.carsVelocity)

            if car.xcor() <= -340:
                self.car_list.remove(car)
                car.clear()
                car.hideturtle()
                del car

        return True

    def next_level(self):
        self.carsVelocity += MOVE_INCREMENT

        for car in self.car_list:
            self.car_list.remove(car)
            car.clear()
            car.hideturtle()
            del car
