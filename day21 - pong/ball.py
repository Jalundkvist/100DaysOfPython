from turtle import Turtle, Screen
from random import choice


# CONSTANTS
EDGE_LIMITER = 20
N_BOUNCES = 3


class Ball(Turtle):
    """ Class for the pong ball """
    def __init__(self, paddle_x_position: int, screen: Screen):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.x_mov = 2
        self.y_mov = 2
        self.bounce_counter = 0
        self.paddle_position = paddle_x_position
        self.screen_height = screen.canvheight
        self.screen_width = screen.canvwidth
        print(screen.canvwidth)
        self.left_score = 0
        self.right_score = 0
        self.recently_bounced = False

    def move(self, *paddles: Turtle):
        """Move the ball and perform collision detection"""
        self._bounce_detection()
        self._paddle_detection(*paddles)
        self._paddle_miss()
        self._increase_speed()
        x, y = self.xcor(), self.ycor()
        self.goto(x+self.x_mov, y+self.y_mov)

    def _bounce_detection(self):
        """Detect ball collision with screen edges"""
        if self.ycor() <= -self.screen_height + EDGE_LIMITER or self.ycor() >= self.screen_height - EDGE_LIMITER:
            self.y_mov = self.y_mov * -1

    def _paddle_detection(self, *paddles: Turtle):
        """ Paddle_detection, used to determine if the ball has connected with either paddle """
        if self.xcor() > self.paddle_position - EDGE_LIMITER or self.xcor() < - self.paddle_position + EDGE_LIMITER:
            for paddle in paddles:
                if self.distance(paddle) <= 45 and not self.recently_bounced:
                    self.recently_bounced = True
                    self.x_mov = self.x_mov * -1
                    self.bounce_counter += 1

                elif self.distance(paddle) <= 50 and not self.recently_bounced:
                    self.recently_bounced = True
                    self.x_mov = self.x_mov * -1
                    self.y_mov = self.y_mov * -1
                    self.bounce_counter += 1

        else:
            self.recently_bounced = False
        print(self.x_mov, self.y_mov)

    def _increase_speed(self):
        if self.bounce_counter > N_BOUNCES:
            self.increase_speed()
            self.bounce_counter = 0

    def _paddle_miss(self):
        """Checks if a paddle has missed the ball"""
        # Right paddle
        if self.xcor() > self.screen_width:
            self.left_score += 1
            print(self.left_score)
            self.reset_ball()
            return

        # Left paddle
        elif self.xcor() < -self.screen_width:
            self.right_score += 1
            print(self.right_score)
            self.reset_ball()
            return

    def reset_ball(self):
        if self.xcor() > self.screen_width-50 or self.xcor() < -self.screen_width+50:
            if self.x_mov > 0:
                self.x_mov = -2
            else:
                self.x_mov = 2
            self.y_mov = choice([-2, 2])
            self.goto(0, 0)

    def increase_speed(self):
        """ Used to slowly increase the difficulty of the game """
        if self.x_mov < 0:
            self.x_mov -= 1
        else:
            self.x_mov += 1
        if self.y_mov < 0:
            self.y_mov -= 1
        else:
            self.y_mov += 1
