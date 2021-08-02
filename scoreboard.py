from turtle import Turtle
FONT = ("Courier", 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.update_scoreboard()
        self.score_label = "Score: " + str(self.score)


    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.score_label = "Score: " + str(self.score)
        self.pencolor("white")
        self.penup()
        self.setposition(0, 270)
        self.pendown()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=FONT)
        self.hideturtle()

    def reset_scoreboard(self):
        # new high score?
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = -1
        self.update_scoreboard()


    # def game_over(self):
    #     self.score_label = "GAME OVER"
    #     self.pencolor("white")
    #     self.penup()
    #     self.setposition(0, 0)
    #     self.pendown()
    #     self.write(self.score_label, align="center", font=FONT)
    #     self.hideturtle()