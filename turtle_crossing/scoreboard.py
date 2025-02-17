from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    def restart_game(self): #if the player has had a head on collision with any car
        self.clear()
        self.level = 1
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))

    def increase_game_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

        

