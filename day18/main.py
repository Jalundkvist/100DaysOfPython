import turtle as t
from random import randint
from time import sleep


def generate_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def shapes():
    no_sides = 3
    for _ in range(10):
        t.color(generate_random_color())

        for _ in range(no_sides):
            tim.forward(100)
            tim.right(360 / no_sides)

        no_sides += 1


def circle(circles):
    tim.pensize(3)
    num = 1
    bw = int(round(255/circles))
    print(bw)
    for _ in range(circles):
        tim.color(bw, bw, bw)
        tim.circle(num)
        tim.left(360/circles)
        tim.forward(1.2)
        num += 360/circles/2.5
        bw += round(360/circles)


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
circle(500)
screen = t.Screen()
screen.exitonclick()
