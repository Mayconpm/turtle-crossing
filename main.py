import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=turtle.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if len(cars.cars) < 30:
        cars.create_car()
    cars.move()

    if turtle.ycor() >= 300:
        turtle.starting_position()
        cars.level_update()
        score.level_update()

    for car in cars.cars:
        if turtle.distance(car) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
