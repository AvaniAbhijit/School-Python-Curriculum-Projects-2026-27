# What is an object?
# An object is a real thing created from the class.

# What is self?
# self means “this object.”

# Task 1: Check the error and add self as a parameter to show_message() function on line 15.
# Task 2: Create Your Own Class withan  Object
#       1. Create a class named Sport
#       2. Print “Welcome to Sports Academy”
#       3. Create an object and call the function

class Pizza:                             # Create a class named Pizza (this is a blueprint)

    def show_message():                  # Define a function inside the class
        print("Welcome to Pizza Shop!")  # This line prints a message

p1 = Pizza()                             # Create an object from the class
p1.show_message()                        # Call the function using the object
                                     
