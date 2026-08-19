from karel.stanfordkarel import *
# exercise turning right w/ new function
# make karel turn right :]
# if function practice, learning with new define/func to create


def turn_right_safe(): # turns whenever right slot is free
     if right_is_clear():
            turn_left()
            turn_left()
            turn_left()
            
def turn_left_safe(): # turns whenever left slot is free
    if left_is_clear():
            turn_left()
            
def move_safe(): # moves to a slot whenever it is free
    if front_is_clear():
        move()

def main():
    while left_is_clear() or front_is_clear():
        while front_is_clear():
            move_safe()
        turn_right_safe()
        turn_left_safe()
        
        
        
   
