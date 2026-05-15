# check_collision() function checks if the basket catches a fruit.
# fruit.distance(basket) checks how close the fruit is to the basket.
# If the fruit is very close (less than 50), it means the basket caught it.
# Then: The fruit disappears. The fruit is removed from the list so it does not appear again.

# Task 1: complete the code from line no 91 to 94 for obstacle collision.



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

# Function to check if the basket touches any fruit
def check_collision():
    for fruit in fruit_list:                    # Check each fruit one by one
        if fruit.distance(basket) < 50:         # If the fruit is close to the basket
            fruit.hideturtle()                  # Hide the fruit
            fruit_list.remove(fruit)            # Remove the fruit from the fruit_list

                                                # Check each obstacle one by one
                                                # If the obstacle is close to the basket
                                                # Hide the obstacle
                                                # Remove the obstacle from the obstacle_list

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
    check_collision()

screen.mainloop()
