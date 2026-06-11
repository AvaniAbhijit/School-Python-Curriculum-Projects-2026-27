# Task 1: Change the car colour from "red" to your favourite colour.
# Hint  : look for car.color("red", "dark red") — change both places!

# Task 2:Make the car bigger! Change forward(120) to forward(180)
#       and see what happens. Do the wheels still look right?

# Task 3:Can you add a second car? Copy the car drawing code,
#       use a new turtle called car2 = turtle.Turtle()
#       and start it at goto(-100, -200) instead.

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
t.penup()
t.goto(-380, -260)
t.setheading(0)
t.color("white")
t.pensize(5)

for i in range(20):
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(20)

# Car Code
car = turtle.Turtle()
car.speed(0)
car.hideturtle()

# --- Car body (big rectangle) ---
car.penup()
car.goto(-300, -200)   # starting position of car
car.pendown()
car.color("red", "dark red")
car.width(5)
car.begin_fill()
for i in range(2):
    car.forward(120)   # width of car
    car.left(90)
    car.forward(40)    # height of car body
    car.left(90)
car.end_fill()

# --- Car roof (smaller rectangle on top) ---
car.penup()
car.goto(-270, -160)   # a bit inside from the body
car.pendown()
car.color("red", "dark red")
car.begin_fill()
for i in range(2):
    car.forward(70)    # roof is smaller than body
    car.left(90)
    car.forward(30)    # roof height
    car.left(90)
car.end_fill()

# --- Left wheel ---
car.penup()
car.goto(-270, -210)   # below the car body
car.pendown()
car.color("black", "white")
car.begin_fill()
car.circle(15)         # circle for wheel
car.end_fill()

# --- Right wheel ---
car.penup()
car.goto(-210, -210)
car.pendown()
car.begin_fill()
car.circle(15)
car.end_fill()


#draw_traffic_lights()
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



