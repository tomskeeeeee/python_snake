from turtle import Turtle
FONT = ("Courier", 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.write_score()
        self.score_label = "Score: " + str(self.score)


    def write_score(self):
        self.score += 1
        self.score_label = "Score: " + str(self.score)
        self.pencolor("white")
        self.penup()
        self.setposition(0, 270)
        self.pendown()
        self.write(self.score_label, align="center", font=FONT)
        self.hideturtle()
