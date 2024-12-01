from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.refresh()
    
    def get_random_food_position(self):
        x_pos = randint(-self.screen_width // 2 + 20, self.screen_width // 2 - 20)
        y_pos = randint(-self.screen_height // 2 + 20, self.screen_height // 2 - 20)
        return (x_pos, y_pos)

    def refresh(self):
        self.goto(self.get_random_food_position())
