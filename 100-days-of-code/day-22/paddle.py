from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, initial_position, shape = "square"):
        super().__init__(shape)
        self.shapesize(stretch_wid=5, stretch_len=1) #5*20 and  1*20
        self.color("white")
        self.penup()
        self.goto(initial_position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
