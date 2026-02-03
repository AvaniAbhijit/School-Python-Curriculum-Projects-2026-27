# What is a List?
# A list is used to store multiple values in one variable.
# A list is written using square brackets [ ].

# Task 1: Create a list and print it.
# Task 2: Print the length of the list.
# Task 3: Print the first item of the list using index.
# Task 4: Print all items in the list using a for loop.

# Creating a List
subjects = ["Coding", "Horticulture", "Robotics"]
print(subjects)

# Length of a List - len() gives the number of items in the list
print(len(subjects))

# Accessing Items using Index - Index starts from 0
print(subjects[0])   # First item
print(subjects[2])   # Third item

# Looping through a List
for sub in subjects:
    print(subjects)

# Adding an Item to the List - append() adds an item at the end of the list
subjects.append("DIY")
print(subjects)

# Removing an Item from the List - remove() removes a specific item from the list
subjects.remove("Horticulture")
print(subjects)
