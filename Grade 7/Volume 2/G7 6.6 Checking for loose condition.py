# Game over condition: if the ball misses the paddle, and reaches the bottom of the screen

# Task: Finish the logic to check for game losing from line no 93.
# Step 1: Check if ball_y > HEIGHT to see if ball went below the screen missing the paddle.
# Step 2: If True, use render() and blit() functions to display the game over message in red.
# Step 3: Exit out of the game while loop


import pygame

# Font setup
pygame.font.init()
font = pygame.font.Font(None, 36)

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
bricks = []

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
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))


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

  ball_x += ball_speed_x
  ball_y += ball_speed_y

  if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).colliderect(
      pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
      ball_speed_y = -ball_speed_y

  for brick in bricks:
      if brick.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
          bricks.remove(brick)
          ball_speed_y = -ball_speed_y

  if ball_x < 0 or ball_x > WIDTH - ball_size:
      ball_speed_x = -ball_speed_x

  if ball_y <= 0:
     ball_speed_y = -ball_speed_y

  if not bricks:
     you_win_text = font.render('You Win', True, (0, 255, 0))
     window.blit(you_win_text,(300,300))
     running = False

  # Game over condition



  pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
  pygame.draw.circle(window, RED, (ball_x, ball_y), ball_size)

  for brick in bricks:
      pygame.draw.rect(window, BLACK, brick)

  pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
