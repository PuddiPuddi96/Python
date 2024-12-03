from turtle import Turtle

MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self, starting_position, finish_line, shape = "turtle"):
        super().__init__(shape)
        self.penup()
        self.seth(90)
        self.finish_line = finish_line
        self.starting_position = starting_position
        self.go_to_start()
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def is_at_finish_line(self, y_finish_line):
        return self.ycor() > y_finish_line

    def go_to_start(self):
        self.goto(self.starting_position)
