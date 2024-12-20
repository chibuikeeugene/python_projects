import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.shapesize(.5, .5)
        self.penup()
        self.randomize_food_location()

    def randomize_food_location(self):
        self.x =  random.randint(-250, 250)
        self.y =  random.randint(-250, 250)
        self.setposition(self.x, self.y)
        


