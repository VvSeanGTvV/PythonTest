# This program manipulates two lists: names and numbers.
# The names list contains various superhero names.
# The numbers list contains a mix of positive and negative numbers.

# Initializing the lists
names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol"]
numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]

# A loop that will output every other name in the names list.
print("Every other name in the names list:")
for i in range(0, len(names), 2):  # Skips every other element by incrementing by 2
    print(names[i])

# A loop that will output only the positive numbers in the numbers list.
print("\nPositive numbers in the numbers list:")
for num in numbers:
    if num > 0:  # Check if the number is positive
        print(num)

# A loop that will output the sum of all the values in the numbers list.
sum_numbers = 0
print("\nSum of all the numbers in the numbers list:") # "\n" is usually nicknamed break line (or new line dependent on how you call it), it is also similar to \r (CRLF line break).
for num in numbers:
    sum_numbers += num  # Adding each number to sum_numbers
print(sum_numbers)

# A loop that will output only the numbers that are odd.
print("\nOdd numbers in the numbers list:")
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        print(num)

# A loop that will output only the names that come before "Thor" in the alphabet from the names list.
# As the name "Thor" is not in the list, we use the alphabetic order condition.
print("\nNames that come before 'Thor' in the alphabet:")
for name in names:
    if name < "Thor":  # Check if the name comes before "Thor" alphabetically
        print(name)

# A loop that will find the minimum and maximum values in the numbers list.
min_value = numbers[0]  # Initializing with the first value of the list to prevent nullification error
max_value = numbers[0]  # Initializing with the first value of the list to prevent nullification error

for num in numbers: # Since it is an array loop throughout the whole numbers list
    if num < min_value:  # If current number is smaller than min_value, update min_value
        min_value = num
    if num > max_value:  # If current number is larger than max_value, update max_value
        max_value = num

print("\nMinimum and maximum values in the numbers list:")
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")


