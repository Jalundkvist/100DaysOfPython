from turtle import Turtle
from time import sleep

START_POS = (0, 275)
TEXT_SIZE = 15
FONT = 'Courier'
TEXT_TYPE = 'bold'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.pencolor("white")

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(START_POS)
        self.write(arg=f"Score: {self.score}", align="center", font=(FONT, TEXT_SIZE, TEXT_TYPE))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=(FONT, TEXT_SIZE*2, TEXT_TYPE))

    def countdown(self, screen):
        self.goto(0, 50)
        for num in range(3, 0, -1):
            self.write(arg=f"{num}", align="center", font=(FONT, TEXT_SIZE * 2, TEXT_TYPE))
            screen.update()
            sleep(1)
            self.clear()

