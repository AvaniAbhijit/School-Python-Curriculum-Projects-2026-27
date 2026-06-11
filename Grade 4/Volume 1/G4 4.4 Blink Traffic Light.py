# Time: The time module helps us make the turtle wait for a few seconds.
#       We can use it to create simple animations and make drawings move slowly.
# While: A while loop keeps doing the same task again and again.

# Task 1: Blink the second light with yellow color using t2 from line 94 onwards.
# Task 2: Blink the third light with green color using t3 from line 106 onwards.

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
t.hideturtle()

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











# Blink third light with green color











turtle.clear()



