# screen.fill on line 26 is used to give the screen color.
# BG_COLOR on line 16 is a tuple variable contaning RGB values.


# Task 1: Change BG_COLOR color on line 16 with value (255, 255, 255).

import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

# Define colors
BG_COLOR = (50, 25, 50)  # Dark purple background


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background color
    screen.fill(BG_COLOR)

    # Update display
    pygame.display.update()

pygame.quit()