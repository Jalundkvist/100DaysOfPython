from turtle import Turtle, Screen


class Scoreboard(Turtle):
    """ Class to handle the score in the pong game """
    def __init__(self, screen: Screen):
        super().__init__()
        self.score = [0, 0]
        self.pu()
        self.hideturtle()
        self.color("white")

    def update_score(self):
        pass