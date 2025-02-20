# Sean Matthew Gomboc 01/28/25

import random  # Importing random to able shuffle the list

# Function definition for compare
def compare(num1, num2):
    if num1 < num2:
        print(f"{num1} is less than {num2}")
    elif num1 > num2:
        print(f"{num2} is less than {num1}")
    else:
        print(f"{num1} is equal to {num2}")

# Create an empty list called names
names = []

for _ in range(3):  # Loop runs 3 times
    # Prompt the user for two integers
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    # Call the compare function and pass the two numbers
    compare(num1, num2)

# Prompt the user for 6 names and append them to the names list
for _ in range(6):
    name = input("Enter a name: ") # Prompts the user for a Name
    names.append(name) # Add it to the names list

# Prompt the user for how many people they want to vote off the island
votes_off = int(input("How many people would you like to vote off the island? "))

# Function definition for eliminate
def eliminate(num_to_eliminate):
    random.shuffle(names)  # Shuffle the list randomly
    for _ in range(num_to_eliminate):
        names.pop()  # Remove one name from the list using pop
    return names  # Return the remaining names

# Call the eliminate function and store the returned list of remaining names
remaining_people = eliminate(votes_off)

# Print the remaining names that were not voted off the island
print("\nRemaining people who were not voted off the island:")
for person in remaining_people:
    print(person)



