from turtle import Turtle, Screen, shape, mainloop
from pandas import *

screen = Screen()
screen.title("U.S. States Game")

image_path = "./asset/blank_states_img.gif"
screen.addshape(image_path) 
shape(image_path)

data = read_csv("./data/50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guess_states)}/50 States Correct", 
        prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        DataFrame(missing_states).to_csv("./data/states_to_learn.csv")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.up()
        state_data = data[data.state == answer_state]
        turtle.goto(state_data.x.item(), state_data.y.item())
        turtle.write(state_data.state.item())
