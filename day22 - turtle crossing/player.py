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
        self.score = 1

    def move_turtle(self):
        if self.ycor() + MOVE_DISTANCE >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.score += 1
        else:
            self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.score = 1
        self.goto(STARTING_POSITION)
