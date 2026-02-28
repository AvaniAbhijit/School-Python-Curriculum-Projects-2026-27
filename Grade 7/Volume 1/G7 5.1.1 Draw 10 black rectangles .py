# Task 1 : Draw 5 black rectangle on the top of the screen with same dimetions as the blue rectangle.

import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

BG_COLOR = (255,255,255)
BLUE = (0,0,255) 
BLACK = (0,0,0)       

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Draws the white rectangle on screen at bottom of the screen.
    pygame.draw.rect(screen, BLUE, (350,550,100,20))    
                                                        # Draw black rectangle 1
                                                        # Draw black rectangle 2
                                                        # Draw black rectangle 3
                                                        # Draw black rectangle 4
                                                        # Draw black rectangle 5


    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()