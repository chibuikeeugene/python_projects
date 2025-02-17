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
scoreboard = Scoreboard()

### defining keypress event
screen.onkey(turtle_player.move, "Up")
screen.listen() # listen for keypress events

game_is_on = True
while game_is_on:
    # setting delay for screen updating
    time.sleep(0.5)
    
    carmanager.create_car()
    carmanager.move()

    # detect a collision when the player hits any of the cars
    for car in carmanager.car_list:
        if car.distance(turtle_player) < 20:
            game_is_on = False # stop the game
            turtle_player.goto(0, 0) # send player to the 0,0 coordinate 
            scoreboard.restart_game()
        # detect when the player has reached the top
        elif turtle_player.ycor() > 280:
            turtle_player.goto(0, -280)
            carmanager.increase_speed()
            scoreboard.increase_game_level()

    screen.update()



screen.exitonclick()