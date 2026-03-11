# goto(x, y) moves the turtle directly to the specified coordinate on the screen.
# x-coordinate is the horizontal position and y-coordinate is the vertical position.
# penup() lifts the turtle’s pen so it can move around the screen without drawing lines.

# Task 1: Uncomment line 22 and run again to observe the change.
# Task 2: Change the coordinate of the basket to move it to the left bottom corner.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)


# Create the basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)  # Basket shape
#basket.penup()
basket.goto(0, -250)

screen.update()
