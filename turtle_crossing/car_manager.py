from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    # defining attributes for our class blueprint
    def __init__(self):
        super().__init__()
        self.car_list =  [] # hold all car blueprints
        self.speed = 10    

    def create_car(self):
        car =  Turtle()
        car.shape('square')
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(300, random.randrange(-250, 250, 10))
        car.setheading(180)
        self.car_list.append(car)
        self.hideturtle()
        
    def move(self):
        for car in self.car_list:
            car.forward(self.speed)
            
    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        self.move()