# The function moves all fruits downward. Each fruit falls by 10 steps.
# If a fruit goes below the screen, it disappears. The fruit is also removed from the fruits list so the game stays clean.
# screen.tracer(0) turns off automatic screen updates.
# This makes the game smoother and faster.
# We use screen.update() later to show all movements together.


# Task 1: Uncomment on line 14 and run the code.
# Task 2: Copy the code from 56 to 60 in move_obstacle function and
#         change fruit to obstacle and fruit_list to obstacle_list.

import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
#screen.tracer(0)

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
    fruit.goto(random.randint(-350, 350), 300)
    fruit_list.append(fruit)

# Create empty Obstacles list
obstacle_list = []

def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("triangle")
    obstacle.color("black")
    obstacle.penup()
    obstacle.goto(random.randint(-350, 350), 300)
    obstacle_list.append(obstacle)

# Move fruits
def move_fruits():
    for fruit in fruit_list:
        fruit.sety(fruit.ycor() - 10)
        if fruit.ycor() < -300:  # Remove fruits that fall below the screen
            fruit.hideturtle()
            fruit_list.remove(fruit)

# Move obstacles
def move_obstacles():
    print("move obstacles")





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
    time.sleep(0.05)
 # Randomly create fruits and obstacles
    if random.randint(1, 20) == 1:
        create_fruit()
    if random.randint(1, 40) == 1:  # Obstacles appear less frequently
        create_obstacle()

    # Move objects
    move_fruits()

screen.mainloop()
