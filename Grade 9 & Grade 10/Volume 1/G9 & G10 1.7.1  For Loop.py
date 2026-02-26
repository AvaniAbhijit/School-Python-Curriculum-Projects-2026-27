# A for loop repeats instructions a fixed number of times.
# range() provides the sequence of numbers the loop follows.

# Task 1: Write a for loop using range() to print on line 16 onwards:
#          1. "Mission 1 Started" to "Mission 5 Started"
#               After the loop, print:
#          2. "All Missions Activated!"


# The game unlocks levels one by one.
for level in range(1, 6):
    print("Level", level, "Unlocked")     # Unlocks Level 1 to 5

print("All Levels Ready!")



