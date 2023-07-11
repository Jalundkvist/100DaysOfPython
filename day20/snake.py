from turtle import Turtle

START_POSITION = (0, 0)
MOVE_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270
SCREEN_RADIUS = 280


class Snake:

    def __init__(self):
        self.snake = []
        self.init_snake()
        self.head = self.snake[0]

    def init_snake(self):
        x, y = START_POSITION
        for i in range(3):
            self.add_segment((x, y))
            x -= 20

    def add_segment(self, position):
        self.snake.append(Turtle(shape="square"))
        self.snake[-1].pu()
        self.snake[-1].color("white")
        self.snake[-1].goto(position)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            self.snake[seg_num].goto(self.snake[seg_num - 1].xcor(), self.snake[seg_num - 1].ycor())
        self.head.forward(20)
        self.snake[-1].color("white")

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def inside_boundaries(self):
        head = self.head
        if head.xcor() > SCREEN_RADIUS or head.xcor() < -SCREEN_RADIUS:
            return False
        elif head.ycor() > SCREEN_RADIUS or head.ycor() < -SCREEN_RADIUS:
            return False
        return True

    def not_collided(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return False
        return True
