import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

MAX_CARS = 2

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkeypress(player.move_turtle, 'Up')


# Counter
counter = 0
amount_of_cars = random.randint(0, MAX_CARS)
cars = []


def car_in_bounds(car_list):
    for car in cars[::-1]:
        car.move_car()
        if car.is_outside():
            car.hideturtle()
            cars.remove(car)


game_is_on = True
while game_is_on:
    if counter < 6:
        counter += 1
    else:
        counter = 0
        amount_of_cars = random.randint(0, MAX_CARS)
        for _ in range(amount_of_cars):
            cars.append(CarManager(screen))
    car_in_bounds(cars)
    time.sleep(0.1)
    screen.update()

