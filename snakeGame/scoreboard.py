from turtle import Turtle
WRITING_COLOR = "white"
ALIGN = "center"
FONT = ["arial", 24, "normal"]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color(WRITING_COLOR)
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()
        self.addScore
    
    def addScore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
    
