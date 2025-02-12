from turtle import Turtle



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self): # defining class attribute
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        # self.hideturtle()

    def move(self): # defining class method - getting the turtle to move
        self.forward(MOVE_DISTANCE)

    