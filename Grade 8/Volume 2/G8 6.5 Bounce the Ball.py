# move(self) method on line 58,in the Ball class moves the ball automatically,
# self.rect.x += self.speed_x → on line 66, Changes x position of ball continously.
# self.rect.y += self.speed_y → on line 67, Changes y position of ball continously.
# On line 60 & 61,The condition checks if the ball’s top has crossed the margin.
# move() method called in the game loop on line 87.

# Task: Write the code for check collision with the bottom of the screen on line 63 onwards.

import pygame
pygame.init()

screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI Game')

BG_COLOR = (50, 25, 50)
WHITE = (255, 255, 255)

# Clock to control frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second
margin = 50

rect_width = 20
rect_height = 100
rect_y = (screen_height - rect_height) // 2

def draw_board():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, WHITE, (0, margin), (screen_width, margin), 2)  # Top margin line

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)  # Paddle dimensions
        self.speed = 5  # Movement speed

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 50:                        # Move up (prevent going above margin line area)
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < screen_height:  # Move down (prevent going below screen)
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)  # Draw paddle

# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)  # Ball size
        self.speed_x = 4
        self.speed_y = -4

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def move(self):
        #check collision with top MARGIN
        if self.rect.top < margin:
            self.speed_y = -self.speed_y
        #check collision with bottom of the screen



        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

right_paddle = Paddle(screen_width - 40, rect_y)
left_paddle = Paddle(20, rect_y)
ball = Ball(screen_width//2,screen_height//2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player paddle
    right_paddle.move(pygame.K_UP, pygame.K_DOWN)

    draw_board()
    right_paddle.draw()
    left_paddle.draw()
    ball.draw()
    ball.move()

    # Update display
    pygame.display.update()
    clock.tick(fps)  # Maintain FPS

pygame.quit()
