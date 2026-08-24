from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_safe(): # moves to a slot whenever it is free
    if front_is_clear():
        move()

def main():
    # Problem 4 - Checkerboard (Dynamic)
    # Works on any Square World. (Empty worlds, idk about exercise variants)
    while no_beepers_present() and front_is_clear(): 
        # While loop breaks loop upon a front block or standing in beeper
        while front_is_clear(): # Loop till no foward slot
            put_beeper()
            move()
            if front_is_clear(): # Extra step when clear
                move()
                if front_is_blocked(): # Works on Odd
                    put_beeper()
        if right_is_clear() and front_is_blocked():
            turn_right()
            if beepers_present(): # Works on Odd
                move()
                turn_right()
                move()
            else: # Works on Even
                move()
                turn_right()
        if left_is_clear() and front_is_blocked():
            turn_left()
            if beepers_present(): # Works on Odd
                move()
                turn_left()
                move()
            else: # Works on Even
                move()
                turn_left()
        if beepers_present(): # Just go up a level
            turn_right()
            if front_is_clear(): # Just to not error in small map
                move()
            if front_is_clear(): # This is only break when Odd
                move()
                turn_left()
    
