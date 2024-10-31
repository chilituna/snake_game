from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

SPEED = 0.1

screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("matopeli")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.set_direction_up)
screen.onkey(key="Down", fun=snake.set_direction_down)
screen.onkey(key="Left", fun=snake.set_direction_left)
screen.onkey(key="Right", fun=snake.set_direction_right)

game_on = True
score.update_scoreboard()
while game_on:
    screen.update()
    if snake.head.xcor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        score.gameover()
        game_on = False
    for square in snake.snake[1:]:
        if snake.head.distance(square) < 10:
            score.gameover()
            game_on = False
    time.sleep(SPEED)
    snake.move(screen)
    if snake.head.distance(food) < 20:
        score.score += 1
        snake.grow_snake(food.color()[0])
        score.update_scoreboard()
        food.refresh()


screen.exitonclick()