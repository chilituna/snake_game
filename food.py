from turtle import Turtle
import random
colors = ["yellow", "red", "blue"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()
        self.shape("circle")
        self.penup()
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.color(random.choice(colors))



