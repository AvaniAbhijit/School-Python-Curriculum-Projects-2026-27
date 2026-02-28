# t.color("green", "red") in line 10 aand 18 , sets the pen color to green (outline color) 
# and the fill color to red (inside color of the shape).

# Task 1: Remove the line coming between the two eyes using penup() in line 15 and
#         pendown() in line 17.

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green","red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.circle(80)
                         # penup() lifts the pen (stops drawing)
t.forward(250)
                         # pendown() puts pen down (starts drawing again)
t.color("green","red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.circle(80)
turtle.done()
