from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def lev_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}")

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="left", font=FONT)

