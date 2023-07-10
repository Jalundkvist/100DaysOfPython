# import colorgram as cg
# quantity = 30
# rgb = []
# colors = cg.extract('spots.jpg', quantity)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
# print(rgb)

import turtle as t
import random

rgb_list = [(249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9),
 (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59),
 (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60),
 (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232),
 (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159),
 (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153)]

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.speed("fastest")
tim.color(random.choice(rgb_list))

screen = t.Screen()
width = -270
height = -250

for h in range(10):
    for w in range(10):
        tim.color(random.choice(rgb_list))
        tim.pu()
        tim.goto(width, height)
        tim.pd()
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        width += 60
    width = -270
    height += 60
screen.exitonclick()

