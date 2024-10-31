from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.show_score()

    def gameover(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

