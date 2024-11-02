STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.pu()
        self.seth(90)
        self.goto(STARTING_POSITION)
        self.next_level()
    def move(self):
        self.forward(MOVE_DISTANCE)
    def next_level(self):
        self.goto(STARTING_POSITION)  

    
