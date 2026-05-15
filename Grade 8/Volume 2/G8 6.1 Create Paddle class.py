# class Paddle defined for the left and right paddles. Has attributes - rect object.
# left_paddle & right_paddle on line 51 and 52 are now objects of Paddle.
#    The object will need only the x and y position of the paddle
#    as the width and height are same for both paddles.
# draw() function on line 36 has been moved into the class which draws
#    the paddle object. This function is called now using the object.

# Task 1: Create the right_paddle instance by passing the x and y coordinates on line no 52.
# Task 2: Call the draw method on right_paddle on line 66 after left_paddle.draw().


import pygame
pygame.init()

# Screen setup
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI Game')

# Colors
BG_COLOR = (50, 25, 50)
WHITE = (255, 255, 255)
margin=50

# Rectangle dimensions
rect_width = 20
rect_height = 100
rect_y = (screen_height - rect_height) // 2

def draw_board():
    screen.fill(BG_COLOR)
    #(0, margin)=0,50 starting point and (screen_width, margin) = 600,50 ending point. 2 is thickness.
    pygame.draw.line(screen, WHITE, (0, margin), (screen_width, margin), 2)  # Top margin line

#def draw():
#    pygame.draw.rect(screen, WHITE, left_paddle)
#    pygame.draw.rect(screen, WHITE, right_paddle)

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, rect_width, rect_height)  # Paddle dimensions

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)  # Draw paddle

#left_paddle = pygame.Rect(20, rect_y, rect_width, rect_height)
#right_paddle = pygame.Rect(screen_width - 40, rect_y, rect_width, rect_height)

left_paddle = Paddle(20, rect_y)
right_paddle = Paddle()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game board
    draw_board()
    # Draw the rectangles
    #draw()
    left_paddle.draw()

    pygame.display.update()

pygame.quit()
