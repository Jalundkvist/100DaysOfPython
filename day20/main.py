from turtle import Screen, Turtle
from time import sleep

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(n=0)

# Turtle setup
segments = []
x, y = 0, 0
for i in range(5):
    print(i)
    segments.append(Turtle(shape="square"))
    segments[i].color("white")
    segments[i].pu()
    segments[i].goto(x, y)
    x -= 20
    screen.update()
sleep(3)


def update_position():
    screen.update()
    sleep(0.2)
    for seg_num in range(len(segments) - 1, 0, -1):
        segments[seg_num].goto(segments[seg_num-1].xcor(), segments[seg_num-1].ycor())


game_on = True
while game_on:
    update_position()
    segments[0].forward(20)
screen.exitonclick()
