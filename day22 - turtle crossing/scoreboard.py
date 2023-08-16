from turtle import Turtle
LEVEL_TEXT_POSITION = (-290, 260)
GAME_OVER_POSITION = (0, 0)

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(LEVEL_TEXT_POSITION)
        self.level = 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.pd()
        self.write(arg=f"LEVEL {self.level}", align="left", font=FONT)
        self.pu()

    def level_up(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.pd()
        self.write(arg="GAME OVER", align="center", font=FONT)
        self.pu()
