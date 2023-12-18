from turtle import Turtle
import random


class Stars(Turtle):
    initial_stars = []

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.stars = []
        self.star_speed = 0.1
        self.initial_star()

    def initial_star(self):
        for _ in range(0, 70):
            star = Turtle("circle")
            star.color("white")
            star.shapesize(stretch_wid=0.05, stretch_len=0.05)
            star.penup()
            random_x = random.randint(-350, 350)
            random_y = random.randint(-450, 450)
            star.goto(random_x, random_y)
            self.initial_stars.append(star)

    def create_stars(self):
        random_chance = random.randint(1, 70)
        if random_chance == 1:
            new_star = Turtle("circle")
            new_star.color("white")
            new_star.shapesize(stretch_wid=0.05, stretch_len=0.05)
            new_star.penup()
            random_x = random.randint(-350, 350)
            new_star.goto(random_x, 500)
            self.stars.append(new_star)

    def move_stars(self):
        for star in self.stars:
            star.goto(star.xcor(), star.ycor() - self.star_speed)

        for star in self.initial_stars:
            star.goto(star.xcor(), star.ycor() - self.star_speed)
