# Task 1: Draw the second light at (15,-30) from line 56 onwards similar to first light.
# Task 2: Draw the third light at (15,-90) from line 64 onwards similar to first and second light.

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

#draw traffic light stand:
t.width(10)
t.color('black')
t.penup()
t.forward(50)
t.right(90)
t.pendown()
t.forward(200)

t.width(0)
t.color('dark grey')
t.hideturtle()

#draw_traffic_lights()

# drawing a first circle light
t1 = turtle.Turtle()
t1.width(5)
t1.penup()
t1.goto(15,30)
t1.pendown()
t1.hideturtle()
t1.circle(20)

# drawing a second circle light







# drawing a third circle light


