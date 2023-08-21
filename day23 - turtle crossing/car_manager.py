import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
SCREEN_BORDER = -300
SCREEN_START = 300
CAR_ZONE = [-250, 250]


def is_outside(car_object):
    if car_object.xcor() < SCREEN_BORDER:
        return True
    return False


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def __del__(self):
        print("DELETING CAR TURTLE")

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle("square")
            car.pu()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setheading(180)
            car.goto(300, random.randint(CAR_ZONE[0], CAR_ZONE[1]))
            self.all_cars.append(car)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        # Reverse for-loop for a more safe approach in removing items from list.
        for car in self.all_cars[::-1]:
            car.forward(self.car_speed)
            if is_outside(car):
                car.hideturtle()
                self.all_cars.remove(car)
