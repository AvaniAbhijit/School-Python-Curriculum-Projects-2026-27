# What is a Function?
# A function is a block of code that runs when we call it.

# Task 1 : Create a function called say_goodbye (without parameter)
#          It should print: "Game Over!" ,"See you next time!"

# Task 2 : Create a function with parameter called favorite_toy
#          It should take toy name as a parameter.
#          It should print: "My favorite toy is" and the toy name.


# A function without parameter does not take any value from outside.
def say_welcome():          # def is a keyword to define function and say_welcome is function name.
    print("Welcome to the Game!") # Function body
    print("Get Ready to Play!")

say_welcome()                     # call the function.

# A function with parameter takes a value and uses it inside the function.
def greet_player(name):
    print("Hello", name)
    print("Let’s start the adventure!")

greet_player("Aarav")   # call the function with name "Aarav".
greet_player("Riya")    # call the function with name "Riya".


                        #Create a function called say_goodbye
                        # print: "Game Over!"
                        # print : "See you next time!"
                        # Call the function.


                        # Create a function with parameter called favorite_toy
                        # print: "My favorite toy is"
                        # Call the function with toy name.
