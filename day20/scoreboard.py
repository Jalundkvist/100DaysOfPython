from turtle import Turtle

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
        self.goto(START_POS)
        self.write(arg=f"Score: {self.score}", align="center", font=(FONT, TEXT_SIZE, TEXT_TYPE))

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(START_POS)
        self.write(arg=f"Score: {self.score}", align="center", font=(FONT, TEXT_SIZE, TEXT_TYPE))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=(FONT, TEXT_SIZE*2, TEXT_TYPE))
