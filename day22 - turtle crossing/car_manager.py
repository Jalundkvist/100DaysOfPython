import random
from turtle import Turtle, Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_BORDER = -300
SCREEN_START = 300
CAR_ZONE = [-260, 260]


class CarManager(Turtle):
    def __init__(self, game_screen: Screen):
        super().__init__()
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(random.randint(SCREEN_START, SCREEN_START+50), random.randint(CAR_ZONE[0], CAR_ZONE[1]))

    def __del__(self):
        print("DELETING CAR TURTLE")

    def is_outside(self):
        if self.xcor() < SCREEN_BORDER:
            return True
        return False

    def move_car(self):
        self.forward(MOVE_INCREMENT)
