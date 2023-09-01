from turtle import Turtle

FONT = ("Courier", 16, "bold")
FONT_GAME_OVER = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=270)
        self.level = 1
        self.write(arg=f"Level = {self.level}", move=False, align="left", font=FONT)

    def level_update(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level = {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg="Game Over", move=False, align="center", font=FONT_GAME_OVER)
