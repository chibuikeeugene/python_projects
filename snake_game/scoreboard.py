from turtle import Turtle
ALIGNMENT =  'center'
FONT =  ('Arial', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        self.color('white')
        self.write(f'Your score: {self.score}', align= ALIGNMENT, font=FONT)
        self.hideturtle()
        
    def if_food_eaten_increase_score(self) -> int:
        self.score += 5
        self.clear()
        self.write(f'Your score: {self.score}', align= ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align= ALIGNMENT, font=FONT)
