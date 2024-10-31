from turtle import Turtle, Screen
import random

STARTING_POSITION = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

colors = ["yellow", "red", "blue"]

class Snake:

    def __init__(self):
        self.snake = []
        self.direction = UP
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_square(pos, random.choice(colors))

    def add_square(self, position, color):
        square = Turtle("square")
        square.penup()
        square.color(color)
        square.goto(position)
        self.snake.append(square)

    def grow_snake(self, color):
        self.add_square(self.snake[-1].position(), color)

    def set_direction_up(self):
        if self.direction != DOWN:
            self.direction = UP

    def set_direction_down(self):
        if self.direction != UP:
            self.direction = DOWN

    def set_direction_left(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def set_direction_right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def move(self, screen):
        for square in range(len(self.snake) - 1, 0, -1):
            x = self.snake[square - 1].xcor()
            y = self.snake[square - 1].ycor()
            self.snake[square].goto(x, y)
        self.head.setheading(self.direction)  # Set heading based on stored direction
        self.head.forward(MOVE_DISTANCE)
