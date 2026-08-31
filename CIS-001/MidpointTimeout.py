from karel.stanfordkarel import *

def mid_point():
    if front_is_clear():
        move()
    if front_is_clear():
        move()
    if front_is_clear():
        mid_point()
    if right_is_blocked():
        turn_left()
        turn_left()
    if front_is_blocked():
        turn_left()
        turn_left()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def main():
    # (Shown by Ben Allen)
    # Problem 5 (Challenge) — Find the Midpoint (No Beeper Help) 
    # Basically we want the function to time out or in this case becomes
    # our try {} catch {} things. Repeating an exact code many times lead
    # to a timeout, acting as our break.
    mid_point()
    turn_right()
    mid_point()
    put_beeper()
    
    # --- Return to Original (except in one row section it inverts to other side)
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    turn_left()
    
