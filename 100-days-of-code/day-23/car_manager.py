from turtle import Turtle, Screen
from random import choice, randint

COLORS = ["red", "yellow", "blue", "black"]
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE = 10

class CarManager:

    def __init__(self, x_cor_starting_position, y_cor_up_range, y_cor_down_range):
        self.cars = []
        self.x_cor_starting_position = x_cor_starting_position
        self.y_cor_up_range = y_cor_up_range
        self.y_cor_down_range = y_cor_down_range
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        if randint(1, 6) % 2 == 0:
            car = Turtle(shape="square")
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            y_cor = randint(self.y_cor_down_range, self.y_cor_up_range)
            car.goto(self.x_cor_starting_position, y_cor)
            self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_DISTANCE

        
