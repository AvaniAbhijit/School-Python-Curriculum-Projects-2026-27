# What is a Tuple?
# A tuple is used to store multiple values in one variable.
# A tuple is written using round brackets( ).

# Task 1: Create a tuple and print it.
# Task 2: Print the length of the tuple.
# Task 3: Print the first item of the tuple using index.
# Task 4: Print all items in the tuple using a for loop.

# Creating a Tuple
num = (11,55,66,33)
print(num)

# Length of a Tuple - len() gives the number of items in the tuple
print(len(num))

# Accessing Items using Index - starts from 0
print(num[0])   # First item
print(num[2])   # Third item

# Looping through a Tuple
for n in num:
    print(num)

# Tuples cannot be changed. We cannot add or remove items from a tuple.
# num.append(99)
