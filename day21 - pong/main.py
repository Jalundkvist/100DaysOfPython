"""
- Create screen
- Create movable paddles
- Create the ball that moves
- Detect collision with wall -> bounce
- Detect paddle miss
- Scoreboard
"""

from turtle import Screen, Turtle

HEIGHT, WIDTH, BG_COLOR = 600, 800, "BLACK"
PDL1_UP, PDL1_DOWN, PDL1_X = "Up", "Down", 350
PDL2_UP, PDL2_DOWN, PDL2_X = "w", "s", -350
PDL_SPEED = 40


def create_screen(height, width, bg_color):
    """ Creates a screen for the pong game """
    pong_screen = Screen()
    pong_screen.bgcolor(bg_color)
    pong_screen.setup(height=height, width=width)
    pong_screen.title("GAME: Pong")
    pong_screen.listen()
    return pong_screen


def paddle_up(pdl: Turtle):
    """ Controls the up movement of the paddle"""
    if pdl.ycor() <= (HEIGHT/2)-70:
        pdl.goto(pdl.xcor(), pdl.ycor() + PDL_SPEED)


def paddle_down(pdl: Turtle):
    """ Controls the down movement of the paddle"""
    if pdl.ycor() >= (-HEIGHT/2)+80:
        pdl.goto(pdl.xcor(), pdl.ycor() - PDL_SPEED)


def create_paddle(up, down, x_position, pong_screen: Screen):
    """ Create a pong paddle and add keybindings for moving"""
    # Create and position turtle
    paddle = Turtle()
    paddle.hideturtle()
    paddle.penup()
    paddle.speed("fastest")
    paddle.shape("square")
    paddle.shapesize(stretch_len=1, stretch_wid=5)
    paddle.goto(x_position, 0)
    paddle.color("white")
    paddle.showturtle()

    # Add keybindings for paddle
    pong_screen.onkey(lambda: paddle_up(paddle), up)
    pong_screen.onkey(lambda: paddle_down(paddle), down)
    return paddle


screen = create_screen(HEIGHT, WIDTH, BG_COLOR)
p1 = create_paddle(PDL1_UP, PDL1_DOWN, PDL1_X, screen)
p2 = create_paddle(PDL2_UP, PDL2_DOWN, PDL2_X, screen)

screen.exitonclick()
