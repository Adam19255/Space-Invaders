from turtle import Turtle


def overlay():
    intro = Turtle()
    intro.color("white")
    intro.penup()
    intro.hideturtle()
    intro.goto(0, 420)
    intro.write("Help protect the galaxy from all the aliens.", align="center", font=("", 20, ""))

    info = Turtle()
    info.color("gray")
    info.penup()
    info.hideturtle()
    info.goto(0, 380)
    info.write("Use arrow keys ⬅➡ to move, 'Space' to fire.", align="center", font=("", 18, ""))

    line = Turtle(shape="square")
    line.color("lime")
    line.shapesize(stretch_wid=0.1, stretch_len=40)
    line.penup()
    line.goto(0, -400)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("lime")
        self.penup()
        self.hideturtle()
        self.score = 0
        overlay()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(280, -430)
        self.write(f"Score: {self.score}", align="center", font=("", 14, ""))

    def add_points(self, points):
        self.score += points
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.color("yellow")
        self.goto(0, 0)
        self.write(f"Game Over!\nScore: {self.score}", align="center", font=("", 30, ""))
