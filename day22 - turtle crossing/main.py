import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

MAX_CARS = 2


def move_cars(car_list, speed_multiplier):
    for car in car_list[::-1]:
        car.move_car(speed_multiplier)
        if car.is_outside():
            car.hideturtle()
            car_list.remove(car)


def collision_check(turtle: Turtle, car: Turtle):
    if turtle.distance(car) < 36 and 20 > turtle.ycor() - car.ycor() > -20:
        return True
    return False


def main():
    # Create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()

    # Create 'player' turtle
    player = Player()
    screen.onkeypress(player.move_turtle, 'Up')

    # Create scoreboard
    scoreboard = Scoreboard()

    # Variables
    counter = 0
    amount_of_cars = random.randint(0, MAX_CARS)
    cars = []
    game_is_on = True

    while game_is_on:
        scoreboard.level(player.score)
        if counter >= 6:
            counter = 0
            amount_of_cars = random.randint(0, MAX_CARS)
            for _ in range(amount_of_cars):
                cars.append(CarManager(screen))

        counter += 1
        move_cars(cars, player.score)
        for car in cars:
            if collision_check(player, car):
                game_is_on = False
        time.sleep(0.1)
        screen.update()

    scoreboard.game_over()
    for car in cars:
        car.hideturtle()
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()