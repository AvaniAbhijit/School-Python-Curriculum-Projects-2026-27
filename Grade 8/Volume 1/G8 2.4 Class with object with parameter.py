# show_message(self, flavour) is a function that belongs to the class 
# and accepts extra information (flavour) when called.

# Task 1: Create Your Own Class with an  Object on 19 onwards.
#       1. Create a class named Sport
#       2. Create a function in the class with self and parameter sport_name.
#       3. Print the sport name inside the funciton.
#       4. Create an object and call the function.


class Pizza:                                # Create a class named Pizza 
    def show_message(self, flavour):        # self + flavour parameter
        print("Welcome to Pizza Shop!")
        print("Your pizza flavour is:", flavour) # pass flavor here to print

p1 = Pizza()                               # Create an object
p1.show_message("Cheese")                  # Call the function and pass flavour

