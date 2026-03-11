# Event handling is making the game respond to a key press or a mouse click.
# Event handling is used to move the basket left and right to catch the falling fruits.

# screen.listen(): on line 42, turtle-screen starts listening for key press.
#   Works with onkey() function.
# screen.onkey(): on line 43, calls a function move_left() when LEFT arrow key is pressed.
# Note: No change in output will be observed.

# Task 1: Write the code on line 45 to call move_right()function when RIGHT arrow key is pressed.

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
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# Create the fruits
fruit1 = turtle.Turtle()
fruit1.shape("circle")
fruit1.color("yellow")
fruit1.penup()
fruit1.goto(-200, 250)

fruit2 = turtle.Turtle()
fruit2.shape("circle")
fruit2.color("green")
fruit2.penup()
fruit2.goto(200, 250)

# Basket Movement
screen.listen()                     # Listen for keyboard input
screen.onkey(move_left, "Left")     # call move_left() when Left arrow is pressed
                                    # call move_right() when Right arrow is pressed


screen.update()


