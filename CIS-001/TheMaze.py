from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    # Problem 3 — Maze Solving
    # Works with Maze & Corridor Exercise
    # Compacted clearing if statements. Using elif (else if)
    while no_beepers_present(): # Loop till stand on one
        if front_is_clear(): # Move when clear
            move()
        elif left_is_clear(): # Turn 90
            turn_left()
        elif right_is_clear(): # Turn 270
            turn_right()
        elif back_is_clear(): # Turn 180
            turn_left()
            turn_left()
    if beepers_present(): # Picks it up whenever it is standing on one
        pick_beeper()
