# Win Condition (if not bricks_list): on line 89 checks if bricks_list is empty, display winning text.
# To display text, follow these steps:
# 1. Initiate the font library to work with text in pygame on line 13
# 2. Create a new font object with default font and size 36 pixels on line 14.
# 3. font.render() on line 90: Creates the text image for text provided; does not display on screen.
# 4. screen.blit() on line 91: Displays the rendered text on pygame screen at (x, y) coordinates.

# Task 1: Make running = False on line 92 to exit from game loop.
# Task 2: Change the winning text, font color, size, type of your choice.

import pygame

pygame.font.init()                      # Initialize the font module.
font = pygame.font.Font(None, 36)       # create font object

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

  ball_x += ball_speed_x
  ball_y += ball_speed_y

  for brick in bricks_list:
      if brick.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
          bricks_list.remove(brick)
          ball_speed_y = -ball_speed_y

  if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).colliderect(
      pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
      ball_speed_y = -ball_speed_y

  if ball_x < 0 or ball_x > WIDTH - ball_size:
      ball_speed_x = -ball_speed_x

  if ball_y <= 0:
     ball_speed_y = -ball_speed_y

  # Winning Condition
  if not bricks_list:        # Empty bricks_list
     you_win_text = font.render('You Win', True, (0, 255, 0)) # Green color winning text
     window.blit(you_win_text,(300,300))                      # Display text in center
                                                              #Exit from the while loop.


  pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
  pygame.draw.circle(window, RED, (ball_x, ball_y), ball_size)

  for brick in bricks_list:
      pygame.draw.rect(window, BLACK, brick)

  pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
