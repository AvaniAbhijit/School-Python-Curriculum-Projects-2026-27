# Drawing a filled green circle using begin_fill() & end_fill().
# begin_fill() starts filling colour inside the shape
# end_fill() completes the filling process

# Task 1: Fill red colour in the smaller circle using begin_fill on line 14 and end_fill on line 16.
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")         # Set the color to green
t.begin_fill()           # Begin to fill color
t.circle(80)
t.end_fill()             # End-filling color
t.color("red")
                         # Begin to fill color
t.circle(50)
                         # End-filling color
turtle.done()
