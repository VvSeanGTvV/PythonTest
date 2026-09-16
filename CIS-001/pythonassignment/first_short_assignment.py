import math

# VvSeanGtvV 09/16/2026

# A1 - Sphere Volume
print("volume = (4/3) * math.pi * radius**3 | radius = 5")
radius = 5
volume = (4/3) * math.pi * radius**3
print(volume)

#A2 - Trig Identity
x = 42
print("(math.cos(x))**2 + (math.sin(x))**2 | x = 42")
print((math.cos(x))**2 + (math.sin(x))**2)

#A3 - One Print, Multiple Variables
# This is the concat way using the +
print("The volume is: " + str((4/3) * math.pi * radius**3) + ", Now we start with this equation ((math.cos(x))**2 + (math.sin(x))**2 | x = 42) it is " + str((math.cos(x))**2 + (math.sin(x))**2))
# This is another way, but are multiple and separated by single space
print("The volume is:", (4/3) * math.pi * radius**3, "Now we start with this equation ((math.cos(x))**2 + (math.sin(x))**2 | x = 42) it is", (math.cos(x))**2 + (math.sin(x))**2)
# This is also another way, but using the 'f' which automatically formats the type to string inside the {}
print(f"The volume is: {(4/3) * math.pi * radius**3}, Now we start with this equation ((math.cos(x))**2 + (math.sin(x))**2 | x = 42) it is {(math.cos(x))**2 + (math.sin(x))**2}")

#B1 - print_right function
# This function has two parameter, but one is a default value (space = 40)
# This function also has parameters that is only accepting specific types not any
def print_right(sentence: str, space: int  = 40):
    remaining: int = space - len(sentence)
    print(" "*remaining+sentence)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")

#B2 - Triangle
def triangle(character: chr, height: int):
    width: int = 1
    for y in range(height):
        trig: str = ""
        for x in range(width):
            trig = trig + character
        print(trig)
        width += 1

triangle('L', 5)

#B3 - Rectangle
def rectangle(character: chr, width: int, height: int):
    for y in range(height):
        rect: str = ""
        for x in range(width):
            rect = rect + character
        print(rect)

rectangle("H", 5, 4)

#B4 - Predict the Error
#def print_twice(string):
#    print(cat) <- it is not using the variable "string"
#    print(cat) <- it is not using the variable "string"

#C1 - for loop "Call triangle in a loop"
for i in range(3):
    triangle("L", 3+i) #start at 3 to 5

#C2 - Bottle Verse
def bottle_verse(number: int):
    #We can use a unique format called \n which indicates a newline that it is actually hidden amongst the text
    print(f"{number} bottles of beer on the wall \n {number} bottles of beer \n Take one down, pass it around")

for n in range(99, 0, -1): # # for n in range(start, end, step)
    bottle_verse(n)
    print()
