# == VS is (Pointer Reference / Same Value)
x = [4, 5] # New
y = x # Shared meaning that y is literally shared with x and any modification to y affects to x as well (or points a reference to x)
z = [4, 5] # New
print(x == z, x is z) 
# x == z is true, despite being two different lists (or array)
# x is z is false, as they are two different lists or array that are mutable/changable
print(x is y) # returns true as they are the same list/mutable array
y.append(6) # adds 6 at end, (due to y = x meaning shared or pointer to x, it also affects x)
print(x == z) # with the new append, from y and since y isshared from x (or y = x) this would now return false as they don't have same values anymore

a = [1, 2, 3] # New
b = a[:] # basically acts as clone this list (not shared)
print(a == b, a is b) # a == b returns true, but a is b returns false as they are two separate list
b[0] = 99 # changes at 0 to 99
print(a) # prints a

#List[List] List on List
a = [1, 2] # New
b = [a, a] # list w/ same pointer list
b[0].append(3) # since 0 is pointer to a, the a appends or adds the 3 at end, same effects to b[1] as it is the same pointer to a
print(b)

# 0 - 2 but they are increment of 1 per f
rows = [] # hi
row = [] # hello
for f in range(3): # we loop this like a grid map but one loop relies on this loop
    for i in range(f+1): # offset by 1 as leaving it 0 results loop skip
        row.append(i) # adds variable i into the array (last)
    rows.append(row) # add that list to rows
    row = [] # reset it bac
print(rows)

rows = [] # hi
row = [] # hello
for i in range(3): #This is also the same but we're cloning the array instead of multi for loops
    row.append(i) # adds variable i into array (last)
    rows.append(row[:]) # Clone the list Row
print(rows)

# Shallow Copy/Clone
grid = [[1, 2], [3, 4]]
shallow = grid.copy() 
# basically grid[:] but are shared, whilist able to make new items into shallow without affecting grid unless using [0][...] to [1][....]
shallow.append([5, 6])
shallow[0][0] = 99
print(grid)
print(shallow)
