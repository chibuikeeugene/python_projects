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
carmanager  = CarManager()

### defining keypress event
screen.onkey(turtle_player.move, "Up")
screen.listen() # listen for keypress events

game_is_on = True
while game_is_on:
    # setting delay for screen updating
    time.sleep(0.5)
    
    carmanager.create_car()
    carmanager.move()

    screen.update()



screen.exitonclick()