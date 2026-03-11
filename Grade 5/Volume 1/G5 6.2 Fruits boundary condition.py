# check fruit boundary condition on line 42
#       if it goes beyond the screen height, hide it on line 43.
# hideturtle() hides the turtle so the object is no longer visible on the screen.

# Task 1: Write the code on line 47 to check the boundary condition for fruit2
#         If it goes beyond the screen, hide it on line 48.


import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)


# Create the basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# Create the fruits
fruit1 = turtle.Turtle()
fruit1.shape("circle")
fruit1.color("yellow")
fruit1.penup()
fruit1.goto(-200, 250)

fruit2 = turtle.Turtle()
fruit2.shape("circle")
fruit2.color("green")
fruit2.penup()
fruit2.goto(200, 250)

def move_fruits():
    y1 = fruit1.ycor()
    fruit1.sety(y1 - 10)
    if fruit1.ycor() < -300:                # Check if fruit1 has crossed the bottom boundary
        fruit1.hideturtle()                 # hide the turtle as it has gone beyond the screen

    y2 = fruit2.ycor()
    fruit2.sety(y2 - 10)
                                            # Check if fruit2 has crossed the bottom boundary
                                            # hide the turtle as it has gone beyond the screen


# Basket Movement
def move_left():
    x = basket.xcor() - 50
    if x > -350:
        basket.setx(x)

def move_right():
    x = basket.xcor() + 50
    if x < 350:
        basket.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

while True:
    screen.update()
    move_fruits()

