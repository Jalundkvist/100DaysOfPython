import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def collision_check(player_turtle: Turtle, car: Turtle):
    if player_turtle.distance(car) < 36 and 20 > player_turtle.ycor() - car.ycor() > -20:
        return True
    return False


def main():
    # Create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()

    # Create 'player' turtle
    player = Player()
    screen.onkeypress(player.move_player, 'Up')

    # Vehicles
    cars = CarManager()

    # Create scoreboard
    scoreboard = Scoreboard()

    # Variables
    game_is_on = True

    # Game on
    while game_is_on:
        # Car logic
        for car in cars.all_cars:
            if collision_check(player, car):
                game_is_on = False
        cars.new_car()
        cars.move_cars()

        # Score logic
        if player.at_finish_line():
            player.goto_start()
            scoreboard.level_up()

        time.sleep(0.1)
        screen.update()

    # Game over
    scoreboard.game_over()
    for car in cars.all_cars:
        car.hideturtle()
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
