# import pygame → Brings the Pygame library into your program so you can use its game features.
# pygame.init() → Starts and prepares all Pygame modules so the game can run properly.
# pygame.display.set_mode() → Creates the game window with the specified width and height.

# Task 1: Define screen_width and screen_height variables on lines 15,16, respectively, 
#         and assign the value 800,600, respectively.
# Task 2: After you run the code, try to close the output window by clicking on the cross button. 

import pygame

# Initialize Pygame
pygame.init()

# Set up game window
                            # width of the game window
                            # height of the game window

# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game window to 'Bricks Game.'
pygame.display.set_caption('Bricks Game')
