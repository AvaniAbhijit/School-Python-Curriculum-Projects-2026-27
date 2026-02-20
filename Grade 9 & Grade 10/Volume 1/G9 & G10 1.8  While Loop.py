# A while loop repeats code as long as a condition is true.

# Task : Create a variable called energy = 3
#       Use a while loop to print:
#      1. "Player can move" while energy is greater than 0
#      2. Decrease energy by 1 each time.
#       After loop ends, print:
#      3. "Player needs rest"

# While Loop
# Phone tries to unlock until correct PIN is entered.
pin = 1234          # Correct PIN stored in system
attempt = 1         # Keeps track of number of attempts
entered_pin = int(input("Enter PIN: ")) # Take PIN input from user (convert text input to integer)

while entered_pin != pin:   # Loop runs while entered PIN is not correct
    print("Attempt", attempt, "- Incorrect PIN")   # Shows wrong attempt message
    attempt = attempt + 1                          # Increase attempt count
    entered_pin = int(input("Enter PIN again: "))  # Ask user to enter PIN again
print("Phone Unlocked")                            # Runs when correct PIN is entered