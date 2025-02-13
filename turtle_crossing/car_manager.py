from turtle import Turtle
from random import randrange


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    # defining attributes for our class blueprint
    def __init__(self):
        super().__init__()
        self.car_list =  [] # hold all car blueprints
        self.cars() # initialize all car prototype
        

    def cars(self):
        for _ in COLORS:
            car =  Turtle()
            car.shape('square')
            car.color(_)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            self.car_list.append(car)
            self.hideturtle()
        
    def move(self):
        for car in self.car_list:
            car.goto(250, randrange(-250, 250, 40))
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)
            
        