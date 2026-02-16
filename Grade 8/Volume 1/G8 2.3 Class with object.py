# What is an object?
# An object is a real thing created from the class.

# What is self?
# self means “this object”

# Task : Create Your Own Class with Object
#       1. Create a class named Sport
#       2. Print “Welcome to Sports Academy”
#       3. Create an object and call the function

class Pizza:                           # Create a class named Pizza (blueprint)

    def show_message(self, flavor):    # Function inside the class
                                      # self → the object using the function
                                      # flavor → value given when function is called
        print("This is", flavor)      # Print the pizza flavor


p1 = Pizza()                          # Create an object from the class

p1.show_message("Cheese")             # Call the function using the object
                                      # "Cheese" is sent as the flavor value

