from turtle import Turtle, Screen
from random import randint

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
TURTLE_SIZE = 20
MAX_X = SCREEN_WIDTH / 2 - TURTLE_SIZE
MIN_X = -SCREEN_WIDTH / 2 + TURTLE_SIZE
MAX_Y = SCREEN_HEIGHT / 2 - TURTLE_SIZE
MIN_Y = -SCREEN_HEIGHT / 2 + TURTLE_SIZE

is_race_on = False

screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > MAX_X:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(randint(0, 10))


screen.exitonclick()
