# In this code we created the empty list and used append list method to add each brick into the list.
# Using for loop , repetition of pygame.draw.rect method has been removed.

# Task 1: Complete the code to add each brick to the bricks_list on line 26,28,30 & 32.



import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

BG_COLOR = (255,255,255)
BLUE = (0,0,255) 
BLACK = (0,0,0) 

bricks_list=[]
# Create a rectangular area object with the dimensions
rect1 = pygame.Rect(10,10, 100, 20)  # This will not draw, but it will define an area.
bricks_list.append(rect1)
rect2 = pygame.Rect(150,10, 100, 20)            # Create rect 2
                                                # append rect 2
rect3 = pygame.Rect(300,10,100,20)              # Create rect 3
                                                # append rect 3
rect4 = pygame.Rect(450,10,100,20)              # Create rect 4
                                                # append rect 4
rect5 = pygame.Rect(600,10,100,20)              # Create rect 5 
                                                # append rect 5
print(bricks_list)                              # Printing bricks_list

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Draws the white rectangle on the screen at the bottom of the screen.
    pygame.draw.rect(screen, BLUE, (350,550,100,20))    
    for brick in bricks_list: 
        pygame.draw.rect(screen, BLACK, (brick))                                             


    # Update the display
    pygame.display.update()

# Quit Pygame

pygame.quit()