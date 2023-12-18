from turtle import Screen, Turtle
from stars import Stars
from scoreboard import ScoreBoard
from ship import Ship
from aliens import Aliens
from shield import Shield
from datetime import datetime
import time

LEVEL = 1
MORE_ROCKETS = 1.5
GAME_IN_ON = False
TIMER = 10
CHANGE_SPEED = False
# Getting the time to now when to increase the speed and rocket count
START_TIME = int(datetime.now().strftime("%S"))

screen = Screen()
screen.setup(width=800, height=1000)
screen.bgcolor("#191919")
screen.title("Space Invaders")
# Turning off the animations so the screen will be ready the moment we start the program
screen.tracer(0)

# Turtle to show the level progres
wave = Turtle()
wave.color("yellow")
wave.penup()
wave.hideturtle()
wave.write(f"Wave {LEVEL} Incoming!\nPress 'Enter' When Ready...", align="center", font=("", 30, ""))

stars = Stars()
scoreboard = ScoreBoard()
ship = Ship()


def start_game():
    global GAME_IN_ON
    if not GAME_IN_ON:
        GAME_IN_ON = True
        wave.clear()
        run_game()


def next_level():
    global LEVEL, MORE_ROCKETS
    LEVEL += 1
    MORE_ROCKETS += 1
    wave.write(f"Level Cleared, +100 Points +life\nWave {LEVEL} Incoming!\nPress 'Enter' When Ready...", align="center",
               font=("", 30, ""))


screen.listen()
screen.onkeypress(ship.move_right, "Right")
screen.onkeypress(ship.move_left, "Left")
screen.onkeypress(ship.fire, "space")
screen.onkeypress(start_game, "\n")


def run_game():
    global GAME_IN_ON, TIMER, CHANGE_SPEED

    aliens = Aliens()
    shield = Shield()

    while GAME_IN_ON:
        # Getting the current time to know when the wanted time have passed
        current_time = int(datetime.now().strftime("%S"))
        TIMER -= 1
        if TIMER == 0:
            # We will see this line alot throughout the while loop because of all the calculations
            # the movement is getting rekt
            aliens.check_change_directions()
            # Added this to make sure the speed change will occur only once (it happens twice but what can we do...)
            CHANGE_SPEED = True
            TIMER = 10

        if (START_TIME - current_time) % 28 == 0 and CHANGE_SPEED:
            aliens.check_change_directions()
            aliens.move_speed *= 0.9
            if (aliens.chance - MORE_ROCKETS) > 20:
                aliens.chance -= MORE_ROCKETS
            # We don't want the whole screen to be with rockets so this is the max allowed
            else:
                aliens.chance = 20
            CHANGE_SPEED = False

        screen.update()
        time.sleep(aliens.move_speed)
        stars.create_stars()
        stars.move_stars()
        aliens.move_aliens()
        ship.move_shot(False)
        aliens.shot_rockets()
        aliens.move_rockets()
        aliens.rocket_miss()
        aliens.check_change_directions()

        if aliens.check_collision_with_ship(ship):
            aliens.check_change_directions()
            ship.lose_life()
            if not ship.all_lives:
                GAME_IN_ON = False
                scoreboard.game_over()

        if aliens.check_collision_with_alien(ship.laser):
            aliens.check_change_directions()
            scoreboard.add_points(10)
            ship.move_shot(True)
            if not aliens.all_aliens:
                GAME_IN_ON = False
                aliens.reset()
                shield.reset()
                ship.reset()
                scoreboard.add_points(100)
                next_level()

        if aliens.check_collision_with_rocket(ship.laser):
            aliens.check_change_directions()
            scoreboard.add_points(5)
            ship.move_shot(True)

        if shield.check_collision_with_laser(ship.laser):
            aliens.check_change_directions()
            ship.move_shot(True)

        aliens.check_collision_with_shield(shield)


screen.mainloop()
