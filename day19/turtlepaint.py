from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def right():
    tim.setheading(0)
    tim.forward(10)


def left():
    tim.setheading(180)
    tim.forward(10)


def up():
    tim.setheading(90)
    tim.forward(10)


def down():
    tim.setheading(270)
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def reset():
    tim.reset()
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


def forward():
    tim.forward(10)


tim.speed(100)
screen.listen()
screen.onkeypress(right, 'Right')
screen.onkeypress(up, 'Up')

screen.onkeypress(down, 'Down')
screen.onkeypress(left, 'Left')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(forward, 'w')
screen.onkey(reset, 'c')

screen.exitonclick()
