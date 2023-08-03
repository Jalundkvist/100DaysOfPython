from turtle import Turtle, Screen


class Paddle(Turtle):
    """ Class for a game paddle to be used for pong """

    def __init__(self, up_key: str, down_key: str, xy_position: tuple, pong_screen: Screen, paddle_speed=20):
        super().__init__()
        self._create_paddle(up_key, down_key, xy_position, pong_screen)
        self.height = pong_screen.window_height()
        self.pdl_speed = paddle_speed

    def _paddle_up(self):
        """ Controls the up movement of the paddle"""
        if self.ycor() <= (self.height/2)-70:
            self.goto(self.xcor(), self.ycor() + self.pdl_speed)

    def _paddle_down(self):
        """ Controls the down movement of the paddle"""
        if self.ycor() >= (-self.height/2)+80:
            self.goto(self.xcor(), self.ycor() - self.pdl_speed)

    def _create_paddle(self, up: str, down: str, xy_position: tuple, pong_screen: Screen):
        """ Create a pong paddle and add keybindings for moving"""
        # Create and position turtle
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(xy_position)
        self.color("white")
        self.showturtle()

        # Add keybindings for paddle
        pong_screen.onkey(self._paddle_up, up)
        pong_screen.onkey(self._paddle_down, down)
