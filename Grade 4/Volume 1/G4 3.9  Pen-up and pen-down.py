# Drawing Two Lines with a Gap using penup() & pendown()
# penup(): Lifts the turtle’s pen — it moves without drawing.
# pendown(): Puts the pen down — it starts drawing again.

# Task 1: Change the gap from 50 to 100 in line 13.
# Task 2: Put a #(hash) before line 12, run again, and notice that lines will get connected.

import turtle
t = turtle.Turtle()
t.forward(100)

t.penup()        # penup() lifts the pen (stops drawing)
t.forward(50)

t.pendown()      # pendown() puts pen down (starts drawing again)
t.forward(100)

turtle.done()
