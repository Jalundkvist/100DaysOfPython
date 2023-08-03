from turtle import Turtle


class GameArt(Turtle):
    """Art for the background of the game screen"""
    def __init__(self, screen_height):
        super().__init__()
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(0, screen_height)
        self.speed("fastest")
        self.shape("square")
        self.pensize(5)
        num_lines = int(screen_height/20)*2
        y_pos = screen_height

        for _ in range(num_lines):
            self.pd()
            y_pos -= 10
            self.goto(0, y_pos)
            self.pu()
            y_pos -= 10
            self.goto(0, y_pos)
