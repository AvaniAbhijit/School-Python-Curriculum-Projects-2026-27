# What is a For Loop?
# A for loop is used to repeat something again and again.
# It helps us check each item one by one in a list.

# Task 1 : Write a for loop to check for your favourite toy in the toys list from line 17 onwards.

# Toy List
toys = ["Car", "Doll", "Ball", "Robot"]
for toy in toys:      # Checks each toy in the toys list.
    print(toy)        # Print each toy from the list

# Print only the toy "Ball" using if condition inside the loop.
for toy in toys:
    if toy == "Ball":       # Checks if ball is there in the toys list or not.
        print("Found the Ball!")



