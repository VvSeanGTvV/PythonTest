from karel.stanfordkarel import *

# Problem 5 — Find the Midpoint
# Basically the beepers become our variable steps
# Works on any Empty Square Maps/world not exercise.
def main():
    # --- Where it starts
    mid_point()
    set_position_to_beeper()
    turn_left()
    turn_left()
    set_position_to_beeper()
    turn_right()
    mid_point()
    set_position_to_beeper()
    turn_left()
    turn_left()
    set_position_to_beeper()
    put_beeper()
    # --- Where it ends
    
    # --- Return to Original (except in one row section it inverts to other side)
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    turn_left()

# --- Functionality
def mid_point(): # we use the beepers as our step counter
    while no_beepers_present():  
        while front_is_clear() and no_beepers_present():
            move()
        if no_beepers_present(): # During the initalize we act it the variable = 0
            put_beeper()
        turn_left()
        turn_left()
        if beepers_present(): # we offset by a space acting as +1 to the variable
            pick_beeper()
            if front_is_clear():
                move()
            put_beeper()
        if front_is_clear():
            move()
        
def set_position_to_beeper(): # the beepers become our set position
    while front_is_clear() and no_beepers_present():
        move()
    if beepers_present():
        pick_beeper()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
