FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.ht()
        self.goto(180,250)
        self.write_score()

    def update_score(self):
        self.score+=1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"SCORE:{self.score}", font=FONT)
        


