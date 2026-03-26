# Use a conditional statement to check that the basket stays within the screen boundary.
# On line 40: x > -350:
# checks if the x-coordinate of the basket is always > the left boundary of the screen

# Task 1: Add the condition on line 45 to stop the basket from moving beyond the right side boundary
# Task 2: Change the boundary check from 350 to 400 (left / right edge of the screen) on lines 40 and 45.

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
def move_left():
    x = basket.xcor() - 50
    if x > -350:                    # Check if the basket has not gone beyond 350 on the left
        basket.setx(x)              # Then only set the new x coordinate position

def move_right():
    x = basket.xcor() + 50
    basket.setx(x)                  # Check if the basket has not gone beyond 350 on the right

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")



screen.update()




