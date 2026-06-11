# Create a White Dashed Road Line from line 88 onwards.

# Task 1: Using penup() Move the turtle to (-380, -260), set the color to white and pen size to 5.
# Task 2: Using for loop ,penup() and pendown(), draw 20 white dashes
#        where each dash is 20 pixels long with a 20-pixel gap between them.

import turtle
import time
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

# drawing a first circle light
t1 = turtle.Turtle()
t1.width(5)
t1.penup()
t1.goto(15,30)
t1.pendown()
t1.hideturtle()
t1.circle(20)

t2 = turtle.Turtle()
t2.width(5)
t2.penup()
t2.goto(15,-30)
t2.pendown()
t2.hideturtle()
t2.circle(20)

t3 = turtle.Turtle()
t3.width(5)
t3.penup()
t3.goto(15,-90)
t3.pendown()
t3.hideturtle()
t3.circle(20)

# Draw Road (Black)
t.penup()
t.goto(350, -200)
t.pendown()
t.color("black")
t.begin_fill()

for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(800)
    t.right(90)

t.end_fill()

# Draw White Dashed Line








while True:

# Blink traffic lights
        t1.fillcolor("red")
        t1.begin_fill()
        t1.circle(20)
        t1.end_fill()

        time.sleep(0.01)

        t1.fillcolor("white")
        t1.begin_fill()
        t1.circle(20)
        t1.end_fill()

        time.sleep(0.01)

# Blink second light with orange color

        t2.fillcolor("yellow")
        t2.begin_fill()
        t2.circle(20)
        t2.end_fill()

        time.sleep(0.01)

        t2.fillcolor("white")
        t2.begin_fill()
        t2.circle(20)
        t2.end_fill()

        time.sleep(0.01)

# Blink third light with green color

        t3.fillcolor("green")
        t3.begin_fill()
        t3.circle(20)
        t3.end_fill()

        time.sleep(0.01)

        t3.fillcolor("white")
        t3.begin_fill()
        t3.circle(20)
        t3.end_fill()

        time.sleep(0.01)









turtle.clear()



