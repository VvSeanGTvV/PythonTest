import random

"""
Sean Matthew Gomboc
02/04/2025
"""

# Function to generate the secret code in 4 digits
def generate_secret_code():
    # Generate a list of 4 random numbers between 1 and 9
    rn = []
    i = 0
    while (i < 4):
        a = random.randint(1, 9)
        if not (a in rn):
            i += 1
            rn.append(a)
        
    return rn

# Function to check how many digits are correct and in the correct place
def check_guess(secret_code, guess):
    i = 0
    c = 0
    d = 0
    spotIndex = ["","","",""]
    # Compare the user's guess with the secret code
    for item in guess:
        try:
            if secret_code[i] == item: 
                spotIndex[i] = "V"
                c = 1
                d += 1
            elif (d < guess.count(secret_code[i])):
                for f in range(4):
                    if secret_code.count(guess[f]) > 0:
                            spotIndex[i] = "!"
                d += 1
            else:
                spotIndex[i] ="X"
        except:
            spotIndex[i] ="X"
        i += 1
    return spotIndex

# Main game function
def play_game():
    secret_code = generate_secret_code()  # Generate the secret code
    tries = 0
    
    print("Welcome to the Mastermind game!")
    print("The secret code consists of 4 different numbers between 1 to 9")
    print()
    print("Game of the Rules:")
    print("V => correct place & correct value")
    print("! => wrong place & correct value")
    print("X => wrong place & wrong value")
    
    while True:
        
        # Prompt the user for their guess
        guess_input = input("Enter your guess (4 digits, each between 1 and 9): ")
        if (len(guess_input) < 4 or len(guess_input) > 4 or not (guess_input.isnumeric())): # Check validation input
            print("Invalid Input")
        else: # if Valid go here
            tries += 1
            # Convert the input into a list of integers
            guess = [int(digit) for digit in guess_input]
            
            # Check how many digits are correct and in the correct place
            correct_digits = check_guess(secret_code, guess)
    
            # Print how many digits are correct
            print(f"{correct_digits}")
            print(f"{correct_digits.count('V')} digits are correct")
            print(f"{correct_digits.count('!')} digits are correct but wrong spot.")
            
            # If all 4 digits are correct, the user has won
            if correct_digits.count('V') == 4:
                print(f"Congratulations! You've cracked the code in {tries} tries.")
                break
            
            if tries > 17:
                print(f"Nice Try! You've tried to crack the code in {tries} tries.")
                break
# Start the game
play_game()


