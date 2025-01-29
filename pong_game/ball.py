from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1,1)
        self.penup()
        self.x_pos = 10 # incremental x position of the ball
        self.y_pos = 10 # incremental y position of the ball

    def move(self):
        x_new = self.xcor() + self.x_pos
        y_new = self.ycor() + self.y_pos
        self.goto(x_new, y_new)

    def change_y_direction(self):
        self.y_pos *= -1

    def change_x_direction(self):
        self.x_pos *= -1

    def reset_position(self):
        self.setposition(0,0)