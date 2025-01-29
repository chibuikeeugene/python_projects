from turtle import Turtle



class Bat(Turtle):
    def __init__(self, bat_coord):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(bat_coord)
   
    def move_bat_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)
        

    def move_bat_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
            
