from karel.stanfordkarel import *
# exercise turning right w/ new function
# make karel turn right :]


def turn_right_safe():
     if right_is_clear():
            turn_left()
            turn_left()
            turn_left()
            
def turn_left_safe():
    if left_is_clear():
            turn_left()

def main():
    while left_is_clear() or front_is_clear():
        while front_is_clear():
            move()
        turn_right_safe()
        turn_left_safe()
        
        
        
   
