# This variation, makes the ball move continously.
# On the line 64, the x-coordinate of the ball is incremented by ball_speed_x
# As it is in game loop, the x-coordinate will continously change for each iteration.

# Task: On line 65, increment the y-coordinate of the ball by ball_speed_y

import pygame


WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

# Bricks
brick_rows = 5
brick_cols = 9
brick_width = 78
brick_height = 20
brick_padding = 10
bricks_list = []

# Ball
ball_size = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

clock = pygame.time.Clock()
FPS = 30  # Set desired frames per second

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + brick_padding
        brick_y = row * (brick_height + brick_padding) + brick_padding
        bricks_list.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))


window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Brick Game')

running = True

while running:
  clock.tick(FPS)
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  window.fill((255,255,255))
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and paddle_x > 0:
    paddle_x -= paddle_speed
  if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
    paddle_x += paddle_speed

  ball_x += ball_speed_x    #continuosly move the ball across the x-axis.
                            #continuosly move the ball across the y-axis.

  pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
  pygame.draw.circle(window, RED, (ball_x, ball_y), ball_size)

  for brick in bricks_list:
      pygame.draw.rect(window, BLACK, brick)

  pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
