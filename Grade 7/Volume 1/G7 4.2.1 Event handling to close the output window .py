# The main loop in a Pygame program keeps the game running.
# It repeats again and again until the player decides to quit.
# We need event handling to listen to the player clicks.
# pygame.event.get() on line 23 listens to - Keyboard input (KEYDOWN, KEYUP),  
# Mouse clicks and Window closing (QUIT event).
# If the player closes the game window, the game quits as on lines 24 and 25.

# Task 1: Write code for another if statement on line 26 to check for event.type == pygame.KEYDOWN: 
# Task 2: When above condition is true, print("You pressed a key! Key Code:", event.key)on line 27.

import pygame
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

# Main loop
running = True
while running:
    for event in pygame.event.get():     # Check for User Quit
        if event.type == pygame.QUIT:
            running = False    
    
    

    pygame.display.update()           # Update display
pygame.quit()                         # Quit Pygame