import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('grey')
screen.setup(width=600, height=600)
screen.tracer(0)
timmy=Player()
cars=CarManager()
score=Scoreboard()
screen.listen()
screen.onkeypress(timmy.move,  "Up")
game_is_on = True

while game_is_on:
    cars.gen_car()
    cars.move_car()
    time.sleep(0.1)
    screen.update()
    if timmy.ycor()>FINISH_LINE_Y:
        timmy.next_level()
        cars.inc_speed()
        score.update_score()
    for car in cars.all_cars:
        if car.distance(timmy)<30:
            game_is_on=False
    


screen.exitonclick()
    
    
    
