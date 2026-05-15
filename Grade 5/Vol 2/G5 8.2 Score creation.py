# This code shows the score at the top of the game screen.
# score_display is a turtle used only for writing text.
# hideturtle() hides the turtle icon so only the score is visible.
# write() displays the score on the screen.

# Task : Change the background color, fruits,obstacle and paddle color.

import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)


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
    for obstacle in obstacle_list:
        obstacle.sety(obstacle.ycor() - 10)
        if obstacle.ycor() < -300:  # Remove obstacles that fall below the screen
            obstacle.hideturtle()
            obstacle_list.remove(obstacle)

score = 0
# Function to check if the basket touches any fruit
def check_collision(score):
    for fruit in fruit_list:
        if fruit.distance(basket) < 50:
            fruit.hideturtle()
            fruit_list.remove(fruit)
            score += 1
# Check each obstacle one by one
    for obstacle in obstacle_list:
        if obstacle.distance(basket) < 50:
            obstacle.hideturtle()
            obstacle_list.remove(obstacle)
            score -= 1
    return score


# Display score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("black")
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 24, "normal"))

# Function to update the score
def update_score(score):
    score_display.clear()       # Clear the old score
    # Write the new score
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

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
    move_obstacles()

    # Check collisions
    score = check_collision(score)

    # Update score display
    update_score(score)

screen.mainloop()
