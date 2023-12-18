from turtle import Turtle, Screen
import random

X_DISTANCE = 40
Y_DISTANCE = 40
ROCKET_MOVE_DISTANCE = 8


class Aliens(Turtle):
    all_aliens = []
    all_rockets = []

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.create_aliens()
        self.move_distance = 10
        self.move_speed = 0.1

        # Creating the rocket shape
        screen = Screen()
        screen.register_shape("rocket", ((0, -20), (-5, 0), (-10, 20), (10, 20), (5, 0)))
        # The initial chance for a rocket to fall
        self.chance = 70

    def create_aliens(self):
        for row in range(0, 3):
            for column in range(0, 8):
                alien = Turtle("arrow")
                alien.color("lime")
                alien.penup()
                alien.setheading(270)
                alien.shapesize(stretch_wid=1.4, stretch_len=1.4)
                alien.goto(-380 + (column * X_DISTANCE), 220 + (row * Y_DISTANCE))
                position = (alien.xcor(), alien.ycor())
                self.all_aliens.append((alien, position))

    def move_aliens(self):
        # enumerate is a built-in Python function that adds a counter to an iterable
        # and returns it in a form of an enumerate object.
        for index, (alien, position) in enumerate(self.all_aliens):
            alien_x, alien_y = position
            new_x = alien_x + self.move_distance
            alien.goto(new_x, alien_y)
            # Updating the array with the new position
            self.all_aliens[index] = (alien, (new_x, alien_y))

    def shot_rockets(self):
        random_chance = random.randint(1, self.chance)
        if random_chance == 1:
            alien = random.choice(self.all_aliens)
            rocket = Turtle("rocket")
            rocket.color("red")
            rocket.penup()
            rocket.setheading(90)
            rocket.shapesize(stretch_wid=0.3, stretch_len=0.4)
            rocket.goto(alien[1])  # Set rocket position to the chosen alien's position
            position = (rocket.xcor(), rocket.ycor())
            self.all_rockets.append((rocket, position))

    def move_rockets(self):
        for index, (rocket, position) in enumerate(self.all_rockets):
            rocket_x, rocket_y = position
            new_y = rocket_y - ROCKET_MOVE_DISTANCE
            rocket.goto(rocket_x, new_y)
            self.all_rockets[index] = (rocket, (rocket_x, new_y))

    def check_change_directions(self):
        for alien, position in self.all_aliens:
            x_axis, y_axis = position
            if x_axis < -380 or x_axis > 370:
                self.move_distance *= -1

    def check_collision_with_ship(self, ship):
        for index, (rocket, position) in enumerate(self.all_rockets):
            if ship.distance(rocket) < 30:
                self.all_rockets.pop(index)
                rocket.hideturtle()
                return True
        return False

    def check_collision_with_alien(self, laser):
        for index, (alien, position) in enumerate(self.all_aliens):
            if alien.distance(laser) < 28:
                self.all_aliens.pop(index)
                alien.hideturtle()
                return True
        return False

    def check_collision_with_rocket(self, laser):
        for index, (rocket, position) in enumerate(self.all_rockets):
            if rocket.distance(laser) < 5:
                self.all_rockets[index] = (rocket, (-1000, 1000))
                self.all_rockets.pop(index)
                rocket.hideturtle()
                return True
        return False

    def check_collision_with_shield(self, shield):
        for index, (rocket, position) in enumerate(self.all_rockets):
            for shield_index, shield_piece in enumerate(shield.all_shield):
                if shield_piece.distance(rocket) < 10:
                    self.all_rockets[index] = (rocket, (-1000, -1000))
                    self.all_rockets.pop(index)
                    rocket.hideturtle()
                    shield.all_shield.pop(shield_index)
                    shield_piece.hideturtle()

    def rocket_miss(self):
        for index, (rocket, position) in enumerate(self.all_rockets):
            rocket_x, rocket_y = position
            if rocket_y < -390:
                self.all_rockets.pop(index)
                rocket.hideturtle()

    def reset(self):
        for index, (alien, position) in enumerate(self.all_aliens):
            self.all_aliens.pop(index)
            alien.hideturtle()

        for index, (rocket, position) in enumerate(self.all_rockets):
            self.all_rockets[index] = (rocket, (-1000, -1000))
            self.all_rockets.pop(index)
            rocket.hideturtle()

        self.all_aliens = []
        self.all_rockets = []
