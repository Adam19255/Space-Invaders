from turtle import Turtle

SHIP_DISTANCE = 40
MOVE_DISTANCE = 10


class Ship(Turtle):
    all_lives = []
    num_of_lives = -1

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("lime")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.goto(0, -340)
        self.lives(2)

        self.laser = Turtle("square")
        self.laser.color("lime")
        self.laser.shapesize(stretch_wid=1, stretch_len=0.1)
        self.laser.penup()
        self.laser.hideturtle()
        self.laser.goto(-1000, -1000)

        self.shot_in_motion = False

    def lives(self, lives):
        for turtle in range(0, lives):
            self.num_of_lives += 1
            ship = Turtle("turtle")
            ship.color("lime")
            ship.penup()
            ship.setheading(90)
            ship.shapesize(stretch_wid=1.5, stretch_len=1.5)
            ship.goto(-380 + (self.num_of_lives * SHIP_DISTANCE), -430)
            self.all_lives.append(ship)

    def move_right(self):
        if self.xcor() < 370:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def move_left(self):
        if self.xcor() > -380:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def fire(self):
        # Making sure there is only one laser at a time
        if not self.shot_in_motion:
            self.laser.showturtle()
            self.laser.goto(self.xcor(), self.ycor() + 30)
            self.shot_in_motion = True

    def move_shot(self, hit):
        if self.shot_in_motion:
            self.laser.goto(self.laser.xcor(), self.laser.ycor() + MOVE_DISTANCE)
            if self.laser.ycor() > 300 or hit:
                self.laser.goto(-1000, -1000)
                self.shot_in_motion = False
                self.laser.hideturtle()

    def lose_life(self):
        if self.all_lives:
            life = self.all_lives.pop()
            life.hideturtle()

    def reset(self):
        self.goto(0, -340)
        self.lives(1)
