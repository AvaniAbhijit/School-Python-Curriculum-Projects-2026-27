# Task 1: Draw a traffic light stand.
# Hint : Set the pen width to 10 and color to black. Move the turtle 50 pixels forward,
#        turn right by 90 degrees, and draw a 200-pixel vertical line.
# Task 2: After drawing, change the pen width to 0, set the color to dark grey, and hide the turtle.

import turtle
t=turtle.Turtle()
#draw blue sky:
turtle.bgcolor("sky blue")
t.penup()
t.goto(180, 180)
t.pendown()
t.color("orange","yellow")
t.width(5)
t.begin_fill()
t.circle(40)
t.end_fill()

#draw traffic light frame and stand:
t.penup()
t.goto(-35, -100)
t.pendown()
t.color("black","dark grey")
t.width(5)
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

# Traffic light stand








