"""
✅ Create screen
✅ Create movable paddles
✅ Create the ball that moves
✅ Detect collision with wall -> bounce
✅ Detect paddle miss
✅ Scoreboard
EXTRA
✅ Ball speed
✅ Change direction of ball when paddle hit on edge
"""

from turtle import Screen
from controller import Paddle
from ball import Ball
from scoreboard import Scoreboard
from gameart import GameArt
from time import sleep

WIDTH, HEIGHT, BG_COLOR = 800, 600, "BLACK"
PDL_POS = int((WIDTH/2-25))
PDL1_UP, PDL1_DOWN, PDL1_XY = "Up", "Down", (PDL_POS, 0)
PDL2_UP, PDL2_DOWN, PDL2_XY = "w", "s", (-PDL_POS, 0)
PDL_SPEED = 40


def create_screen(height, width, bg_color):
    """ Creates a screen for the pong game """
    pong_screen = Screen()
    pong_screen.bgcolor(bg_color)
    pong_screen.setup(width=width, height=height)
    pong_screen.tracer(0)
    pong_screen.title("GAME: Pong")
    pong_screen.listen()

    return pong_screen


def main():
    # Create screen, paddles and ball
    screen = create_screen(HEIGHT, WIDTH, BG_COLOR)
    p1, p2 = Paddle(PDL1_UP, PDL1_DOWN, PDL1_XY, screen, PDL_SPEED), \
        Paddle(PDL2_UP, PDL2_DOWN, PDL2_XY, screen, PDL_SPEED)
    ball = Ball(PDL_POS, screen)
    scoreboard = Scoreboard(screen)
    GameArt(HEIGHT)
    scoreboard.update_score(ball.left_score, ball.right_score)

    while True:
        screen.update()
        if scoreboard.score != [ball.left_score, ball.right_score]:
            scoreboard.update_score(ball.left_score, ball.right_score)
        ball.move(p1, p2)
        sleep(0.01)


if __name__ == "__main__":
    main()
