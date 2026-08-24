from karel.stanfordkarel import *


def main():
    # Problem 1 - Row Cleanup
    # Works on: Harvest Field | Beeper Pile | Beeper Piles
    while beepers_present() or no_beepers_present():
        while front_is_clear() and no_beepers_present():
            move()
        if beepers_present():
            pick_beeper()
        if front_is_blocked():
            turn_left()
            move()
            turn_left()
