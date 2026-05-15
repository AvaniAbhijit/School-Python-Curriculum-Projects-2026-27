# random helps the fruits appear in different colors and different positions whenever the game runs.
# The lines in create_fruit() function are the same used to create fruit1 and fruit2.
# fruits are created as long as the game runs and are getting appened to the fruits list
# create_fruit() and create_obstacle() functions,create fruits,obstacles randomly.


# Task 1: Create obstacle_list = [] on line 39.
# Task 2: Complete the code on line 48 & 49 by refering the code on 37 & 38.

import turtle
import random

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

# Fruits list and properties
fruit_list = []
fruit_colors = ["red", "yellow", "green", "orange"]

def create_fruit():
    fruit = turtle.Turtle()
    fruit.shape("circle")
    fruit.color(random.choice(fruit_colors))
    fruit.penup()
    fruit.goto(random.randint(-350, 350), 300)  # Put the fruit at a random position at the top of the screen
    fruit_list.append(fruit)                    # Add the fruit to the fruits list

# Create empty Obstacles list


def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("triangle")
    obstacle.color("black")
    obstacle.penup()
                                                # Put the obstacle at a random position at the top of the screen
                                                # Add the obstacles to the obstacle_list.


#def move_fruits():
#    y1 = fruit1.ycor()
#    fruit1.sety(y1 - 10)
#    if fruit1.ycor() < -300:
#       fruit1.hideturtle()
#    y2 = fruit2.ycor()
#    fruit2.sety(y2 - 10)
#     if fruit2.ycor() < -300:
#       fruit2.hideturtle()

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

     # Randomly create fruits and obstacles
    if random.randint(1, 20) == 1:
        create_fruit()
    if random.randint(1, 40) == 1:  # Obstacles appear less frequently
        create_obstacle()

# Close the screen on click
screen.mainloop()


