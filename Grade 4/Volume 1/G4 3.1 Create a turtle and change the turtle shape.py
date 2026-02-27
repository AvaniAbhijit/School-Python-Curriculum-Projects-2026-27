# There are total 7 different shapes of turtle
# turtle,square,triangle,circle,classic,arrow,blank
# by default shape of turtle is classic

# Task 1: Change the shape of the turtle in line 10 to "square".
# Task 2: put a #(hash) before the line 10 ,run again and notice that the default shape is "classic".

import turtle       # import turtle module to use turtle features
t = turtle.Turtle() # Creating a turtle
t.shape("turtle")   # Giving the shape
turtle.done()       # To keep the output screen open
