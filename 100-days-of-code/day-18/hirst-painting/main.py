from colorgram import extract
from turtle import Screen, Turtle, colormode
from random import choice


def get_rgb_colors_from_image(path, color_number=10):
    colors_from_image = extract(path, color_number)
    rgb_colors_from_image = []

    for color in colors_from_image:
        rgb_color_tuple = (
            color.rgb[0],
            color.rgb[1],
            color.rgb[2]
        )
        rgb_colors_from_image.append(rgb_color_tuple)
    
    return rgb_colors_from_image


colors = get_rgb_colors_from_image('imgs/painting.png', 10)

turtle = Turtle()
turtle.shape("triangle")
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

screen = Screen()
screen.screensize(600, 600)

colormode(255)

# Set initial position
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

x_pos_original = turtle.pos()[0]

for index in range(10):
    y_pos = turtle.pos()[1] + 50
    turtle.setposition(x_pos_original, y_pos)
    for _ in range(10):
        turtle.dot(20, choice(colors))
        turtle.forward(50)


screen.exitonclick()
