# Conditional statements: Python decides which code to run based on whether a condition is True or False.
# Operators: Symbols used to compare values or combine conditions in Python.


# COMPARISON OPERATORS
# > (Greater than), < (Less than), >=  (Greater than or equal to), <=  (Less than or equal to)
# ==  (Equal to), !=  (Not equal to)

# LOGICAL OPERATORS
# and → All conditions must be True, or  → Any one condition must be True, 
# not → Reverses the condition (True becomes False)


# Task 1: Run the program and observe the output.
# Task 2: Change the values of age, score, lives, and bonus.

# Example 1: Simple if-else condition
# This checks if the age is 13 or more

age = 14

if age >= 13:
    print("You can play this game.")
else:
    print("You are too young to play.")


# Example 2: if-elif-else (Multiple conditions)
# This checks performance based on score

score = 75

if score >= 90:
    print("Excellent Performance")
elif score >= 70:
    print("Good Performance")
else:
    print("Needs Practice")


# Example 3: Using logical operator AND
# Both conditions must be True to continue the game

lives = 1
bonus = False

if lives > 0 and bonus == False:
    print("You can continue playing.")
else:
    print("Game Over!")


# Example 4: Using logical operator OR
# Only one condition needs to be True

extra_life = True

if lives > 0 or extra_life:
    print("Second chance given!")
else:
    print("No chances left.")


# Example 5: Using NOT operator
# NOT reverses the condition

game_over = False

if not game_over:
    print("Game is running.")
else:
    print("Game stopped.")
