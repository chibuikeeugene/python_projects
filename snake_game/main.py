from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# creating a screen object
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('green')
screen.title('My Snake Game')

screen.tracer(0) # turn off screen animation

snake = Snake() # create a snake object

food = Food() # create a food object

scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, 'i')
screen.onkey(snake.down, 'k')
screen.onkey(snake.left, 'j')
screen.onkey(snake.right, 'l')


continue_game =  True
while continue_game: # running a continuous loop for snake object's movement

    # update screen after every .2secs delay
    screen.update() 
    time.sleep(0.1)

    snake.move() # call the snake moove method to move it

    # check the condition for which food can be said to have been eaten by the snake
    if snake.head.distance(food) < 15:
        food.randomize_food_location()
        scoreboard.if_food_eaten_increase_score()
        snake.grow()

    # define wall boundaries for which if hit, brings the game over
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        continue_game = False
        scoreboard.game_over()

        # if snake collides with its own body
        
    

    





screen.exitonclick()