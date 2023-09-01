from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shape("square")
            car.color(choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            y_position = randint(-240, 240)
            car.goto(300, y_position)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            if car.xcor() >= -310:
                car.forward(self.move_distance)
            else:
                y_position = randint(-240, 240)
                car.goto(300, y_position)

    def level_update(self):
        self.move_distance += MOVE_INCREMENT

    def distance(self, turtle):
        for car in self.cars:
            if turtle.distance(car) < 10:
                return True
        else:
            return False
