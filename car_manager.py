COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_Y_RANGE=(-240,240)
import random
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.current_step=STARTING_MOVE_DISTANCE 
        self.ht()
        
    
    def gen_car(self):  
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.current_step)
    
    def inc_speed(self):
        self.current_step+=MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(self.current_step)
        


    
