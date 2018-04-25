grid = [[-1] * 8 for n in range(8)]  # list comprehension
grid[0][0] = 1
grid[7][7] = 1

w = 70  # width of each cell


def draw(screen):
    x, y = 0, 0  # starting position

    for row in grid:
        for col in row:
            if col == 1:
                # print('a')
                screen.fill((250, 0, 0))
            else:
                screen.fill((255))
                pygame.draw.rect(screen, WHITE, [x, y, w, w])
            x = x + w  # move right
        y = y + w  # move down
        x = 0  # rest to left edge

#
# def mousePressed(mouseX, mouseY):
#     grid[int(mouseY / w)][int(mouseX / w)] = -1 * grid[int(mouseY / w)][int(mouseX / w)]
#     # integer division is good here!
#


# from pygame import *
# screen=display.set_mode((600,400))
# running=True
# while running:
#     for evnt in event.get():
#         if evnt.type == QUIT:
#             running=False
#     x,y=mouse.get_pos()
#     b=mouse.get_pressed()
#     if evnt.type == MOUSEBUTTONDOWN:
#         if evnt.button == 1:
#             screencopy=screen.copy()
#     if b[0] == 1:
#         screen.blit(screencopy,(0,0))
#         draw.circle(screen,(255,0,0),(x,y),20)
#     display.flip()
# quit()



# Import a library of functions called 'pygame'
import pygame
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [800, 600]
screen = pygame.display.set_mode(size)


def mousePressed(mouseX, mouseY):
    grid[int(mouseY / w)][int(mouseX / w)] = 1
    # integer division is good here!


pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    screen.fill(WHITE)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('x:', x, ' |  y:', y)
                mousePressed(x, y)

    x, y = 0, 0  # starting position

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] > 0:
                pygame.draw.rect(screen, RED, [x, y, w, w])
            pygame.draw.rect(screen, BLACK, [x, y, w, w], 2)

            x = x + w  # move right
        y = y + w  # move down
        x = 0  # rest to left edge

    # # All drawing code happens after the for loop and but
    # # inside the main while done==False loop.
    #
    # # Clear the screen and set the screen background
    #
    # # Draw on the screen a GREEN line from (0,0) to (50.75)
    # # 5 pixels wide.
    # pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)
    #
    # # Draw on the screen a GREEN line from (0,0) to (50.75)
    # # 5 pixels wide.
    # pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    #
    # # Draw on the screen a GREEN line from (0,0) to (50.75)
    # # 5 pixels wide.
    # pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], True)
    #
    # # Draw a rectangle outline
    # pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    #
    # # Draw a solid rectangle
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    #
    # # Draw an ellipse outline, using a rectangle as the outside boundaries
    # pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
    #
    # # Draw an solid ellipse, using a rectangle as the outside boundaries
    # pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
    #
    # # This draws a triangle using the polygon command
    # pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
    #
    # # Draw an arc as part of an ellipse.
    # # Use radians to determine what angle to draw.
    # pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi / 2, 2)
    # pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi / 2, pi, 2)
    # pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3 * pi / 2, 2)
    # pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)
    #
    # # Draw a circle
    # pygame.draw.circle(screen, BLUE, [60, 250], 40)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()