from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0

    def move_score_position(self,x,y):
        self.goto(x,y)
        self.write(self.score, font=("Impact Regular",60,"normal"))


    def score_up(self):
        self.clear()
        self.score += 1
        self.write(self.score, font=("Impact Regular",60,"normal"))