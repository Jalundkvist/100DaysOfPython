from random import randrange
from turtle import Turtle

SIZE = 0.5


class Food(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen.addshape("apple.gif")
        self.shape("apple.gif")
        self.penup()
        self.shapesize(stretch_len=SIZE, stretch_wid=SIZE)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x, random_y = \
            randrange(-280, 281, 20), \
            randrange(-280, 281, 20)
        self.goto(random_x, random_y)
