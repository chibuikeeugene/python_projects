from turtle import Turtle, Screen
import time
from snake import Snake

# creating a screen object
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My snake game')

screen.tracer(0) # turn off screen animation

snake = Snake() # create a snake object

screen.listen()
screen.onkey(snake.up, 'i')
screen.onkey(snake.down, 'k')
screen.onkey(snake.left, 'j')
screen.onkey(snake.right, 'l')

continue_game =  True
while continue_game: # running a continuous loop for snake object's movement

    # update screen after every .2secs delay
    screen.update() 
    time.sleep(0.2)

    snake.move()

    


screen.exitonclick()