# ycor(): Returns the current y-coordinate (vertical position) of the turtle.
# sety(): Changes the turtle's y-coordinate, moving it up or down.
# move_fruits() function on line 38 uses ycor() and sety() to decrease the y-coordinate of
#                the fruits to make them fall
# while True: on line 63 keeps the program running continuously

# Task 1: Write the code on line 45, 46 to make the fruit2 drop down inside move_fruits() function.
# Task 2: Uncomment line 63 and indent lines 64 and 65 to make them as body of while loop
#         Run and observe the change.

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

def move_fruits():                     # Function to move the fruits down on the screen
    y1 = fruit1.ycor()                 # Get the current y-coordinate (vertical position) of fruit1
    fruit1.sety(y1 - 10)               # Move fruit1 down by decreasing y1 by 10 and set the new value

                                        # Get the current y-coordinate of fruit2 in y2.
                                        # Move fruit2 down by decreasing y2 by 10 and set the new value

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

#while True:
screen.update()
move_fruits()                       # Calls the function to move both fruits down once




