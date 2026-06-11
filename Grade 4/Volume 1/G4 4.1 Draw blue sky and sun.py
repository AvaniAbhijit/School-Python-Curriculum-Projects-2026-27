# In line number 14 we used goto() function
# The goto() function in Python Turtle moves the turtle
# to a specific position on the screen using x and y coordinates.

# Task 1: Create a yellow sun using the turtle,(draw a yellow filled circle).
# Hint : Use color(), begin_fill(), circle(), and end_fill().

import turtle
t=turtle.Turtle()

#draw blue sky:
turtle.bgcolor("sky blue")  #Background color
t.penup()
t.goto(180, 180)
t.pendown()

#draw sun

