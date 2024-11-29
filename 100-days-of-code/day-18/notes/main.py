from turtle import Turtle, Screen, colormode
from random import choice, randint


def random_color():
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )

TURTLE_DIRECTIONS = [0, 90, 180, 270]

turtle = Turtle()
turtle.shape("triangle")
colormode(255)

screen = Screen()

#Draw a square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)

#Draw a dashed line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

#Draw shapes
# for index in range(3, 11):
#     turtle.color(random_color())
#     for _ in range(index):
#         turtle.forward(100)
#         turtle.right(360 / index)

#Draw random walk
# turtle.pensize(20)
# turtle.speed(50)
# for _ in range(200):
#     turtle.color(random_color())
#     turtle.forward(50)
#     turtle.setheading(choice(TURTLE_DIRECTIONS))


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.seth(turtle.heading() + size_of_gap)

turtle.speed("fastest")
draw_spirograph(5)

screen.exitonclick()
