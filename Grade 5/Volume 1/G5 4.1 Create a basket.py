# shape() – It is used to choose the shape of the turtle object.
# Example: "square" makes the turtle look like a square.

# shapesize() – It is used to change the size of the shape. Takes 2 parameters:
# stretch_wid = 1 → keep the height normal
# stretch_len = 5 → make the shape 5 times longer horizontally (width)
# The default square shape turtle is 20 pixels(width) × 20 pixels(height).
# stretch_len = 5 → width = 5 × 20 = 100 pixels

# Task 1: Try all the turtle shapes(circle,classic,turtle,arrow) on line 21.
# Task 2: Uncomment line 23 and run the code.
# Task 3: Change the basket's stretch_width to 3 on line 23. Run and observe the change.

import turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")

basket = turtle.Turtle()   # Create a turtle object called basket
basket.shape("square")   # Set the basket shape to square
basket.color("brown")   # Change the color of the basket
#basket.shapesize(stretch_wid=1, stretch_len=5)   # Stretch the square to make it look like a basket
