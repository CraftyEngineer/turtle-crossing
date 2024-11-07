FONT = ("Courier", 20, "normal")
ALIGN="center"
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("turtle-crossing-start/data.txt") as data:
            self.high_score=int(data.read())
        self.penup()
        self.ht()
        self.goto(0,250)
        self.write_score()

    def update_score(self):
        self.score+=1
        self.write_score()
        if self.score > self.high_score:
            self.high_score=self.score
            with open("turtle-crossing-start/data.txt", mode='w') as data:
                data.write(f"{self.high_score}")

    def write_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} HIGH SCORE: {self.high_score} ", move=False, align=ALIGN, font=FONT)
        


