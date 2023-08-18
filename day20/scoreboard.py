from turtle import Turtle
from time import sleep

START_POS = (0, 275)
FONT = ('Courier', 15, 'bold')
FONT_LARGE = ('Courier', 15, 'bold')
ALIGNMENT = "center"



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="high_score.txt", mode='r', encoding='utf8') as file:
            self.high_score = int(file.readline())
        self.hideturtle()
        self.pu()
        self.pencolor("white")

    def update_scoreboard(self):
        self.clear()
        self.goto(START_POS)
        self.write(arg=f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="high_score.txt", mode='w', encoding='utf8') as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT_LARGE)

    def countdown(self, screen):
        for num in range(3, 0, -1):
            self.goto(0, 50)
            self.write(arg=f"{num}", align=ALIGNMENT, font=FONT_LARGE)
            screen.update()
            sleep(1)
            self.update_scoreboard()

