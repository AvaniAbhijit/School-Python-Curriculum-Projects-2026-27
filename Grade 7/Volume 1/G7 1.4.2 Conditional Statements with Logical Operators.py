# Conditional statements help Python take decisions.

# LOGICAL OPERATORS
# and → All conditions must be True
# or  → Any one condition must be True
# not → Reverses the condition (True becomes False)

# Task 1: Change bonus to True on line 13 and observe the output.
# Task 2: Uncomment line 21. Write the code line 23 onwards using the OR operator.


lives = 1
bonus = False

# Using logical operator AND, check if lives is more than zero AND there is no bonus.
if lives > 0 and bonus == False:          # It is checking both conditions are true.
    print("You can continue playing.")
else:
    print("Game Over!")

#extra_life = False
# Using logical operator OR, check if there is extra_life or if lives is more than zero.
                                        # Check if any one condition must be True.



