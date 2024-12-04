from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.__get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.__set_high_score()
        self.score = 0
        self.update_scoreboard()
    
    def __get_high_score(self):
        high_score = 0
        with open(file="files/data.txt", mode="r") as file:
            high_score = int(file.read())
        return high_score

    def __set_high_score(self):
        with open(file="files/data.txt", mode="w") as file:
            (file.write(f"{self.high_score}"))



    
