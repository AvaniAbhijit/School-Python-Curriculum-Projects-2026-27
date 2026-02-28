# pygame.Rect() used to create a rectangular area object with the tuple (x, y, width, height)
# It makes the code cleaner as the Rect object can be passed to pygame.draw.rect()
# rect1 is the rectangular object created for the first black rectangle.

# Task 1: Complete the code from 24 to 27 to create other rect objects.
# Task 2: Replace the tuple (x, y, width, height) from line 40 to 43 with respective rect objects.


import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

BG_COLOR = (255,255,255)
BLUE = (0,0,255) 
BLACK = (0,0,0) 

# Create a rectangular area object with the dimensions
rect1 = pygame.Rect(10,10, 100, 20)  # This will not draw, but it will define an area.
                                     # Create rect 2
                                     # Create rect 3
                                     # Create rect 4
                                     # Create rect 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Draws the white rectangle on screen at bottom of the screen.
    pygame.draw.rect(screen, BLUE, (350,550,100,20))    
    pygame.draw.rect(screen, BLACK, rect1)                                                
    pygame.draw.rect(screen, BLACK, (150,10, 100, 20))                                                  
    pygame.draw.rect(screen, BLACK, (300,10,100,20))                                                   
    pygame.draw.rect(screen, BLACK, (450,10,100,20))                                                  
    pygame.draw.rect(screen, BLACK, (600,10,100,20))                                                   


    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()