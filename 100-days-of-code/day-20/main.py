from turtle import Turtle, Screen
from time import sleep
from snake import Snake


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

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
    
screen.exitonclick()
