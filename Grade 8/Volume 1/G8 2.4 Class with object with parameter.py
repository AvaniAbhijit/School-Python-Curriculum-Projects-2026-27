





class Pizza:                                # Create a class named Pizza 
    def show_message(self, flavour):        # self + flavour parameter
        print("Welcome to Pizza Shop!")
        print("Your pizza flavour is:", flavour) # pass pflavor here to print

p1 = Pizza()                               # Create an object
p1.show_message("Cheese")                  # Call the function and pass flavour

