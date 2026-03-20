# xcor() returns the current x-coordinate (horizontal position) of the turtle on the screen.
# setx() changes the turtle's x-coordinate, moving it left or right without changing its y-position.
# On line 44, move_left() function is called when the LEFT arrow key is pressed.
# On line 45 it determines xcor() of the turtle and decreases it by 50 steps(pixels).
# On line 46, it uses setx() to set the new position of the turtle, to left of its current position.

# Task 1: Define the function move_right() on line 48 and write the function body to
#         Calculate the x-coordinate using xcor() and add 50 to it
#         Set the new position of the basket using setx()
# Task 2: Change 50 to 20 and observe the speed of the turtle movement when arrow key is pressed.
# Task 3: Change the Left and Right controls on lines 54 and 55 to 'a' and 'd' keys. Run and observe.

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
def move_left():             # function to move left
    x = basket.xcor() - 50   # Get the current x position of basket and subtract 50 to move left
    basket.setx(x)           # Move the basket to the new x position

                             # function to move right
                             # Get the current x position of basket and add 50 to move right
                             # Move the basket to the new x position


screen.listen()                     # Listen for keyboard input
screen.onkey(move_left, "Left")     # call move_left() when Left arrow is pressed
screen.onkey(move_right, "Right")   # call move_right() when Right arrow is pressed



screen.update()



