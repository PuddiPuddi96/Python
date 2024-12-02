from turtle import Turtle

FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"

class Scoreboar(Turtle):

    def __init__(self, visible = False):
        super().__init__(visible=visible)
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    
    def score_point(self, to_left=False, to_right=False):
        if to_left:
            self.left_score += 1
        elif to_right:
            self.right_score += 1
        self.update_scoreboard()
