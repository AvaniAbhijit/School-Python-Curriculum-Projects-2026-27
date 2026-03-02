# Turtle is a Python module that is used to draw shapes and pictures.
# import is a command that helps to use the turtle module in Python.
# Turtle has 7 different shapes - 
#   1. turtle, square, triangle, circle, classic, arrow, blank
#   2. By default shape of the turtle is classic

# Task 1: Change the shape of the turtle in line 12 to "square".
# Task 2: Put a #(hash) before line 12, run again, and notice that the default shape is "classic".

import turtle       # import turtle module to use turtle features
t = turtle.Turtle() # Creating a turtle
t.shape("turtle")   # Giving the shape
turtle.done()       # To keep the output screen open
