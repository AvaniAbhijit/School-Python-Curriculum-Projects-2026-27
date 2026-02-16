# What is a Global Variable?
# A global variable is created outside the function.
# It can be used inside and outside the function.

# Why do we use Global Variables?
# 1. When we want to use the same variable in many functions.
# 2. When we want to share data across the whole program.
# 3. It helps avoid creating the same variable repeatedly.

# Task 1: Call the function on line 18  and print its output on line 19.
# Task 2: Assign a different value to the score variable on line 25 
#         and call the function on line 26.

score = 100                                 # Create a global variable

def show_score():                           # Use it inside a function
    print("Current Score is:", score)
                                            # Call the function
                                            # Print it outside the function


# Change the global variable inside the function
def update_score():
    global score
                                            # Assign a different value to the score variable.
                                            #Call the function

# Print updated value
print("Updated Score:", score)
