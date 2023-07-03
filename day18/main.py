from turtle import Turtle, Screen, colormode
from random import randint
from time import sleep


def generate_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


colormode(255)
t = Turtle()
no_sides = 3

for _ in range(10):
    R, G, B = generate_random_color()
    t.color((R, G, B))

    for _ in range(no_sides):
        t.forward(100)
        t.right(360 / no_sides)

    no_sides += 1
sleep(5)
