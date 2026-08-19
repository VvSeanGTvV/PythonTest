from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    # Problem 3 — Maze Solving
    # Works with Maze & Corridor Exercise
    # Compacted clearing if statements.
    while no_beepers_present(): # Looping unless standing on one
        if front_is_clear():
            move()
        elif left_is_clear():
            turn_left()
        elif right_is_clear():
            turn_right()
        elif back_is_clear():
            turn_right()
    if beepers_present(): # Picks it up whenever it is standing on one
        pick_beeper()
            
        
