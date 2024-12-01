from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food(screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH)

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()
    
screen.exitonclick()
