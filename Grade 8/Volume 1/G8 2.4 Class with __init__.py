# What is __init__?
# __init__ is a special function that runs automatically when an 
# object is created.
# It is used to give starting values to the object.
# It helps each object store its own data.

# Task 1 : Create Two Sport Objects for the class Sport.
#          Create two sports: Cricket and Basketball


class Pizza:                              # Create a class named Pizza (blueprint)

    def __init__(self, flavor):           # Special function that runs when object is created
        self.flavor = flavor              # Store the flavor inside this object

    def show_message(self):               # Function to display pizza information
        print("This pizza is", self.flavor)   # Use stored flavor and print message


p1 = Pizza("Cheese")                     # Create object p1 with flavor "Cheese"
p2 = Pizza("Pepperoni")                  # Create object p2 with flavor "Pepperoni"

p1.show_message()                        # Object p1 runs function → uses its own flavor
p2.show_message()                        # Object p2 runs function → uses its own flavor
