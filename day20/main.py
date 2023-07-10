from snake import Snake
from turtle import Screen
from time import sleep

snake = Snake()


def init_screen():
    game_screen = Screen()
    game_screen.setup(width=600, height=600)
    game_screen.bgcolor("black")
    game_screen.title("Snake game")
    game_screen.tracer(n=0)
    game_screen.listen()
    game_screen.onkey(snake.up, "Up")
    game_screen.onkey(snake.down, "Down")
    game_screen.onkey(snake.left, "Left")
    game_screen.onkey(snake.right, "Right")
    return game_screen


# Screen setup
screen = init_screen()

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move()
