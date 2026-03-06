# pygame.draw.circle(screen,color,(x,y),radius) is used to draw a circle on the screen.

# Task : Draw the ball on the screen using pygame.draw.circle() on line 57.
#       1. The function should take screen as first parameter; followed by:
#       2. Use RED as the color.
#       3. Use ball_x and ball_y as a tuple for the position of the ball.
#       4. Use ball_radius for the size of the ball.
#       5. Write the code inside the game loop so the ball appears on the screen.

import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks Game')

BG_COLOR = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)

# Ball settings
ball_x = 400
ball_y = 500
ball_radius = 10

brick_width = 78
brick_height = 20
brick_padding = 10

bricks_list=[]

for row in range(0,7):
    for col in range(0,9):
        brick_x = col * (brick_width + brick_padding)
        brick_y = row * (brick_height + brick_padding)

        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
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

    # Draw ball


    pygame.display.update()

pygame.quit()
