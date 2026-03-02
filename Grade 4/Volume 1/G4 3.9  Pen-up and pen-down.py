# penup(): Lifts the turtle’s pen — it moves without drawing on a line 11.
# pendown(): Puts the pen down — it starts drawing again on line 14.

# Task 1: Change the gap from 50 to 100 in line 12.
# Task 2: Put a #(hash) before line 11, run again, and notice that lines will get connected.

import turtle
t = turtle.Turtle()
t.forward(100)

t.penup()        # penup() lifts the pen (stops drawing)
t.forward(50)

t.pendown()      # pendown() puts pen down (starts drawing again)
t.forward(100)

turtle.done()
