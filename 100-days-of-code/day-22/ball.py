from turtle import Turtle

class Ball(Turtle):

    def __init__(self, screen_height, screen_width, shape = "circle"):
        super().__init__(shape)
        self.color("white")
        self.penup()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    def bounce(self, on_x=False, on_y=False, on_paddle=False):
        if on_x:
            self.x_move *= -1
        if on_y:
            self.y_move *= -1
        if on_paddle:
            self.move_speed *= 0.9

    def reset_position(self, go_to_left=False, go_to_right=False):
        self.goto(0, 0)
        self.move_speed = 0.1
        if go_to_left:
            self.bounce(on_x=True)
        if go_to_right:
            self.bounce(on_x=True)
