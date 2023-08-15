from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_turtle(self):
        if self.ycor() + MOVE_DISTANCE >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
        else:
            self.forward(MOVE_DISTANCE)
