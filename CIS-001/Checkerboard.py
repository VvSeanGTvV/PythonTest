from karel.stanfordkarel import *

def move_safe(): # moves to a slot whenever it is free
    if front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    # Problem 2 — Checkerboard (8x8)
    # Only works on Even numbers
    while no_beepers_present():
        put_beeper()
        if front_is_clear():
            move_safe()
        else:
            turn_left()
            move_safe()
            turn_left()
        if beepers_present():
                turn_left()
                move_safe()
                move_safe()
                turn_right()
    while beepers_present():
        if front_is_clear():
            if beepers_present():
                pick_beeper()
                move_safe()
            move_safe()
        if front_is_blocked():
            turn_right()
            move_safe()
            turn_right()
            if no_beepers_present():
                turn_right()
                move_safe()
                move()
                turn_left()
            
            
    
       
