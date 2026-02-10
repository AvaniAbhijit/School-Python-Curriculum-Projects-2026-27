# A function is a block of code that performs a specific task.
# We use functions to avoid repeating the same code again and again.
# 1. def is used to create a function
# 2. Function without parameter does not take input on line 14.
# 3. Function with parameter takes value while calling on line 22.


# Task 1: Change the value of player_power from 30 to 50 or 100
#          Run the program and observe the output.

# Task 2: Create a new function named game_over()
#         It should print: "Game Over! Try Again."

# Function without parameter
def start_game():
    print("Game Started!")
    print("Get ready to boost your power")

# Function with parameter
def show_power(power):
    print("Your current power is:", power)

# Calling the function without parameter
start_game()

# Creating a variable to store power value
player_power = 30

# Calling the function with parameter
show_power(player_power)
