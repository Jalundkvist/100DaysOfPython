from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from time import sleep


def init_screen():
    """Screen init function"""
    game_screen = Screen()
    game_screen.setup(width=600, height=600)
    game_screen.bgcolor("black")
    game_screen.title("Snake game")
    game_screen.tracer(0)
    game_screen.listen()
    game_screen.onkey(snake.up, "Up")
    game_screen.onkey(snake.down, "Down")
    game_screen.onkey(snake.left, "Left")
    game_screen.onkey(snake.right, "Right")
    return game_screen


# Game setup
snake = Snake()
screen = init_screen()
food = Food(screen)
scoreboard = Scoreboard()
scoreboard.countdown(screen)
# Game logic
while snake.inside_boundaries() and snake.not_collided():
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

# Game over
scoreboard.game_over()
screen.update()
screen.exitonclick()
