from turtle import Turtle, Screen
from time import sleep

START_POS = (0, 260)
TEXT_SIZE = 15
FONT = 'Courier'
TEXT_TYPE = 'bold'


class Scoreboard(Turtle):
    """ Class to handle the score in the pong game """
    def __init__(self, screen: Screen):
        super().__init__()
        self.score = [0, 0]
        self.pu()
        self.hideturtle()
        self.color("white")
        self.screen = screen

    def update_score(self, p1_score, p2_score):
        self.score = [p1_score, p2_score]
        self.clear()
        self.goto(START_POS)
        self.write(arg=f"{self.score[0]}     {self.score[1]}", align="center", font=(FONT, TEXT_SIZE+10, TEXT_TYPE))
        self.countdown(self.screen)

    def countdown(self, screen):
        self.goto(0, 50)
        for num in range(3, 0, -1):
            self.write(arg=f"{num}", align="center", font=(FONT, TEXT_SIZE * 2, TEXT_TYPE))
            screen.update()
            sleep(1)
            self.color("black")
            self.write(arg=f"{num}", align="center", font=(FONT, TEXT_SIZE * 2, TEXT_TYPE))
            self.color("white")
