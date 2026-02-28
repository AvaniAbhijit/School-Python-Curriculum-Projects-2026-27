# On line no 41 pygame.draw.rect() is used to draw a rectangle shape.
# This method takes 3 parameters:
#   - where to draw: the screen object
#   - Color of the shape: BLUE
#   - rectangular area : tuple : (x_coordinate, y_coordinate, width, height)
# The x and y coordinates are the values of the top left position of the rectangle

# Task 1 : Create a BLUE tuple on line 24 with value (0,0,255) and then run the code.
# Task 2 : Change the position of the rectangle to bottom of the screen 
#          by changing values on line 34.


import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

BG_COLOR = (255,255,255)
                           # Create a tuple BLUE.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Draws the white rectangle on screen.
    pygame.draw.rect(screen, BLUE, (200,150,100,20))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()