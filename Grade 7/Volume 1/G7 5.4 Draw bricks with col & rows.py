# In this code, we are creating the bricks on the screen using columns and rows with nested for loop.

# Task 1: To add a gap between bricks, add padding to the brick_width and brick_height.
# Task 2: Change the range in the for loop to fill half screen with bricks on line 28 and 29.

import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

BG_COLOR = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)

# Bricks layout settings
brick_width = 78
brick_height = 20
brick_padding = 10    # It will give space between two bricks

bricks_list=[]

# Create a rectangular area object with the dimensions
# Create and store each brick using nested loops
for row in range(0,3):  # Loop through each row
    for col in range(0,5):  # Loop through each column
        # Calculate brick's x and y position
        brick_x = col * brick_width
        brick_y = row * brick_height

        # Create a brick as a rectangle
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)

        # Add the brick to the bricks list
        bricks_list.append(brick)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, BLUE, (350,550,100,20))
    for brick in bricks_list:
        pygame.draw.rect(screen, BLACK, (brick))

    pygame.display.update()

pygame.quit()
