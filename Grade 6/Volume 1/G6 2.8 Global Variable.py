# What is a Global Variable?
# A global variable is created outside the function.
# It can be used inside and outside the function.

# Why do we use Global Variables?
# 1. When we want to use the same variable in many functions.
# 2. When we want to share data across the whole program.
# 3. It helps avoid creating the same variable again and again.

# Task 1: Create a function to decrease the score by 50 on line 42 onwords.
# Task 2: Print the final score after decreasing.

# Create a global variable
score = 100

# Use it inside a function
def show_score():
    print("Current Score is:", score)

show_score()

# Print it outside the function
print("Score Outside Function:", score)

# Change the global variable inside function
def update_score():
    global score
    score = 200

update_score()

# Print updated value
print("Updated Score:", score)

# Add 30 to score
def add_bonus():
    global score
    score = score + 30

add_bonus()
print("Score After Bonus:", score)
