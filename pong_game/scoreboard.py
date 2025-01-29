from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.goto(-100, 280)
        self.write(f"{self.l_score}", align='left', font=('Arial', 20, 'normal'))
        self.goto(100, 280)
        self.write(f"{self.r_score}", align='right', font=('Arial', 20, 'normal'))
        self.hideturtle()

    # award points to the left bat
    def l_point(self):
        self.clear()
        self.l_score += 2
        self.update_scoreboard()

    # award points to the right bat
    def r_point(self):
        self.clear()
        self.r_score += 2
        self.update_scoreboard()
