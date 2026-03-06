# If paddle_x becomes less than 0, we set it to 0 so the paddle does not move 
# outside the left side of the screen.
# If paddle_x becomes greater than screen_width - paddle_width, 
# we set it back so the paddle stays inside the right side of the screen.


# Task : Restrict the paddle from moving outside the right side of the screen.
#       1. Check if paddle_x becomes greater than screen_width - 100.
#       2. If this happens, set paddle_x equal to screen_width - 100 so the paddle stays 
#       inside the screen.


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

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT]:         
        paddle_x -= paddle_speed    

    # Move paddle right
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # Restrict paddle from left edge
    if paddle_x < 0:
        paddle_x = 0

    # Restrict paddle from right edge
    


    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y,100,20))
    for brick in bricks_list:
        pygame.draw.rect(screen, BLACK, (brick))

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.update()

pygame.quit()
