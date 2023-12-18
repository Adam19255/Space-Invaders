from turtle import Turtle

X_DISTANCE = 17
Y_DISTANCE = 17


class Shield(Turtle):
    all_shield = []

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.create_shield()

    def create_shield(self):
        for position in range(0, 7):
            for row in range(0, 5):
                for column in range(0, 5):
                    shield = Turtle("square")
                    shield.color("lime")
                    shield.shapesize(stretch_wid=0.4, stretch_len=0.7)
                    shield.penup()
                    shield.goto(-350 + (column * X_DISTANCE) + (position * 100), 0 - (row * Y_DISTANCE))
                    self.all_shield.append(shield)

    def check_collision_with_laser(self, laser):
        for shield_index, shield_piece in enumerate(self.all_shield):
            if shield_piece.distance(laser) < 10:
                self.all_shield.pop(shield_index)
                shield_piece.hideturtle()
                return True
        return False

    def reset(self):
        for shield_index, shield_piece in enumerate(self.all_shield):
            self.all_shield.pop(shield_index)
            shield_piece.clear()
            shield_piece.hideturtle()
        self.all_shield = []
