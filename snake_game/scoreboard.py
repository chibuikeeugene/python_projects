from turtle import Turtle
ALIGNMENT =  'center'
FONT =  ('Arial', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, 270) # x = -150
        self.score = 0
        with open("/Users/eugene/Personal_Projects/python_projects/snake_game/highest_score.txt", mode="r") as fin:
            self.high_score = int(fin.read())
        self.color('white')
        self.update_scoreboard()
        self.hideturtle()
        
    def if_food_eaten_increase_score(self) -> int:
        self.score += 5
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align= ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Your score: {self.score}   High score: {self.high_score}', align= ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # write the current high score to a file
            with open("/Users/eugene/Personal_Projects/python_projects/snake_game/highest_score.txt", mode= 'w+') as fout:
                fout.write(str(self.high_score))
        self.update_scoreboard()
