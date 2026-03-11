# Task 1: Create two new turtles called fruit1 and fruit2 from line 24 onwards.
#         Give them different colors and circle shapes.
#         Place the fruits at the top of the screen using goto().
#         Make sure it does not draw any line while moving to the top.


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
basket.shapesize(stretch_wid=1, stretch_len=5)  # Basket shape
basket.penup()
basket.goto(0, -250)

#Create turtle fruit1






#Create turtle fruit2






screen.update()

