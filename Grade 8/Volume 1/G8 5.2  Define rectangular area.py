# pygame.Rect() used to create a rectangular area object with the tuple (x, y, width, height)
# It makes the code cleaner as the Rect object can be passed to pygame.draw.rect()

# Task 1: Create another WHITE vertical rectangle object - rect2 on line 25.
# Task 2: Draw rect2 below rect1, making it look like a 'T on line 38.'

import pygame

pygame.init()

screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI Game')

BG_COLOR = (50, 25, 50)
WHITE=(255,255,255)

# Rectangle position
rect_x = 200    # x coordinate where the rectangle starts
rect_y = 100    # y coordinate where the rectangle starts

# Create a rectangular area object with the dimensions
rect1 = pygame.Rect(rect_x, rect_y, 200, 50) # This will not draw, but it will define an area.



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Replace the tuple with the rectangular area object - rect1
    pygame.draw.rect(screen, WHITE, rect1)


    # Update the display
    pygame.display.update()

# Quit Pygame

pygame.quit()

