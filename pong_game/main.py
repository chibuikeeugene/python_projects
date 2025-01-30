from turtle import Screen, Turtle
from bat_logic import Bat
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()


screen.setup(800,600)
screen.bgcolor('black')
screen.title('My Ping Pong')

screen.tracer(0)

BAT1_COORD =  (350,0) # starting coordinates for each bat
BAT2_COORD =  (-350,0)

bat1 = Bat(BAT1_COORD) # creating our first bat object
bat2 = Bat(BAT2_COORD) # creating our second bat object
ball = Ball() # creating the ball 
scoreboard = Scoreboard() # creating the score board object

# centre divide dashed line
centre_divide = Turtle()
centre_divide.color('white')
centre_divide.penup()
centre_divide.goto(0, -300)
centre_divide.left(90)
for _ in range(300):
    centre_divide.forward(20)
    centre_divide.penup()
    centre_divide.forward(20)
    centre_divide.pendown()
centre_divide.hideturtle()


screen.listen()

screen.onkey(bat1.move_bat_up, 'Up')
screen.onkey(bat1.move_bat_down, 'Down')
screen.onkey(bat2.move_bat_up, 'w')
screen.onkey(bat2.move_bat_down, 's')
game_is_on =  True

while game_is_on:
    #get the ball to kickstart
    ball.move()

    # detect collision with wall
    if ball.ycor() == 280.0 or ball.ycor() == -280.0:
        ball.change_y_direction()

    # detect collision with the bat
    if ball.distance(bat1) < 50 and ball.xcor() > 330 or ball.distance(bat2) < 50 and ball.xcor() < -330:
        ball.change_x_direction()

    # detect when bat1 misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when bat2 misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    time.sleep( ball.ball_speed) # delay code execution for x secs
    screen.update() #  and refresh screen content


    
    





screen.exitonclick()