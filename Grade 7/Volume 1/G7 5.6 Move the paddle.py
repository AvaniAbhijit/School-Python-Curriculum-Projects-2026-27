# pygame.key.get_pressed() returns the state of key pressed
#       — True if the key is pressed, False if not.
# keys[pygame.K_LEFT] returns True if LEFT ARROW key is pressed on line 59
# If the LEFT ARROW is pressed, we decrease the x value of the paddle making it move left on line 60

# Task 1: Write code on line 63 to check if the RIGHT ARROW key is pressed
#        If so, increase the x value of the paddle making it move right on line 64
# Task 2: Try moving the ball too by changing the ball_x and ball_y
#           by random values inside the while loop

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

ball_x = 400
ball_y = 500
ball_radius = 10

# paddle settings
paddle_x = 350              # x axis value of the paddle
paddle_y = 550              # y axis value of the paddle
paddle_speed = 3            # pixels by which the paddle moves left or right

brick_width = 78
brick_height = 20
brick_padding = 10

bricks_list=[]

for row in range(0,7):
    for col in range(0,10):
        brick_x = col * (brick_width + brick_padding) + brick_padding
        brick_y = row * (brick_height + brick_padding) + brick_padding

        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks_list.append(brick)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    keys = pygame.key.get_pressed() # check for the keys pressed

    if keys[pygame.K_LEFT]:         # check if LEFT ARROW is clicked
        paddle_x -= paddle_speed    # reduce the x position of the paddle

    # Move the paddle to the right when RIGHT ARROW is clicked
                                    # check if RIGHT ARROW is clicked
                                    # increase the x position of the paddle


    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y,100,20))
    for brick in bricks_list:
        pygame.draw.rect(screen, BLACK, (brick))

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.update()

pygame.quit()
