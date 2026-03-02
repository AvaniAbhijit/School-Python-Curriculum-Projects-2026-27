# In this code, we will remove the line that is coming between two Hulk eyes,
# using penup() and pendown().

# Task 1: Complete the code on lines 14 and 16.

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()
t.circle(80)
                         # Use penup() to lift the pen.
t.forward(250)
                         # Use pendown() to put the pen down.
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()
t.circle(80)
turtle.done()

