import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

turtle_player =  Player()

turtle.onclick()

game_is_on = True
while game_is_on:
    time.sleep(0.1)


    # turtle_player.move()
    screen.update()



screen.exitonclick()