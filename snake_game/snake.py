from turtle import Turtle
from time import time

STARTING_COORDINATES = [(0,0), (-20,0), (-40,0)]
DISTANCE =  20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(Turtle):
    def __init__(self) -> None: # initialize a new snake with these attributes
        super().__init__()
        self.snake_segments = [] # holds all the new snake segment
        self.create_snake()
        self.head = self.snake_segments[0] # the first segment of the snake body now refered to as the head
        self.tail = self.snake_segments[-1]
        self.hideturtle() # used to hide the default turtle obj created by snake_segments - which is a cursor
        

    def create_snake(self): # creates the individual parts of the snake
        for coord in STARTING_COORDINATES:
            new_segment =  Turtle()
            new_segment.color('white')
            new_segment.shape('square')
            new_segment.penup()
            new_segment.goto(coord)
            self.snake_segments.append(new_segment)

    def move(self): # makes the snake to move
        for index in range(len(self.snake_segments) - 1, 0, -1):
            x_cor, y_cor = self.snake_segments[index - 1].position()
            self.snake_segments[index].goto(x_cor, y_cor)

        self.head.forward(DISTANCE)
    
    def grow(self): # increase snake length as it feeds
        new_body = Turtle()
        new_body.color('white')
        new_body.shape('square')
        new_body.penup()
        x_cor, y_cor = self.tail.position()
        new_body.teleport(x_cor, y_cor)
        self.snake_segments.append(new_body)

    def up(self): # changes the snake direction to up with a keypad stroke
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self): # changes the snake direction to down with a keypad stroke
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self): # changes the snake direction to right with a keypad stroke
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self): # changes the snake direction to left with a keypad stroke
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

