from turtle import Turtle, Screen
import random

# Variables for turtles
racing = False
colors = ["blue", "green", "red", "yellow", "purple", "orange"]
x, y = -240, -100

# Screen setup
screen = Screen()
screen.setup(width=500, height=400, startx=0, starty=0)

# User prompt
while True:
    bet = screen.textinput(title='Make your bet',
                           prompt=f'Which turtle will win the race? '
                                  f'{" / ".join([color.title() for color in colors])} '
                                  f'- Enter a color: ').lower()
    if bet in colors:
        break

# Initiate turtles
turtles = []
racing = True

# Generate turtles
for i, color in enumerate(colors):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].pu()
    turtles[i].color(color)
    turtles[i].goto(x, y)
    y += 30

# Racing logic
while racing:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if bet == turtle.pencolor():
                print(f"You win! The winner is {turtle.pencolor()}")
            else:
                print(f"You lost! The winner is {turtle.pencolor()}")
            racing = False
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)




screen.exitonclick()
