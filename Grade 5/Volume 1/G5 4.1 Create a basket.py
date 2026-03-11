# shape() – It is used to choose the shape of the turtle object.
# Example: "square" makes the turtle look like a square.

# shapesize() – It is used to change the size of the shape.
# Example: stretch_len=5 makes the shape longer.

# Task 1: Try all the turtle shapes(circle,classic,turtle,arrow) on line 18.
# Task 2: Change the basket color for the shape on line 19.
# Task 3: Uncomment line 20 and run the code.

import turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")

basket = turtle.Turtle()   # Create a turtle object called basket
basket.shape("square")   # Set the basket shape to square
basket.color("brown")   # Change the color of the basket
#basket.shapesize(stretch_wid=1, stretch_len=5)   # Stretch the square to make it look like a basket


