import pygame
from pygame.locals import *


# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def boardInit(n, grid_size):
    grid = [[-1] * n for i in range(n)]  # list comprehension
    w = grid_size  # width of each cell
    return grid, w


def mousePressed(mouseX, mouseY, player):
    grid[int((mouseY - y_start) / w)][int((mouseX - x_start) / w)] = player


def drawBoard():
    x, y = x_start, y_start  # starting position

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, BLUE, [x, y, w, w])
            elif grid[row][col] == 2:
                pygame.draw.rect(screen, RED, [x, y, w, w])

            pygame.draw.rect(screen, BLACK, [x, y, w, w], 2)
            x = x + w  # move right
        y = y + w  # move down
        x = x_start  # rest to left edge


def writePlayer(player_name, screen):
    message = "Player " + str(player_name) + ": "
    font = pygame.font.SysFont("Lato Semibold", 36)
    text = font.render(message, True, BLACK)
    textpos = screen.get_rect().centerx - int(text.get_rect().centerx*1.5), int(y_start/5)
    screen.blit(text, textpos)

    color_text, color_pos = writePlayerColor(player_name, text.get_rect().centerx)
    screen.blit(color_text, color_pos)


def writePlayerColor(player_name, text_reg):
    font = pygame.font.SysFont("Lato Semibold", 36)
    if player_name == 1:
        message = "blue"
        text = font.render(message, True, BLUE)
    else:
        message = "red"
        text = font.render(message, True, RED)
    textpos = screen.get_rect().centerx + int(text_reg*0.5), int(y_start/5)
    return text, textpos


# Initialize the game engine
pygame.init()
n = 6
grid_size = 50
x_start, y_start = int(grid_size/2), grid_size
grid, w = boardInit(n, grid_size)

# Set the height and width of the screen
size = [grid_size*n + 2*x_start, int(grid_size*n + y_start + x_start)]
screen = pygame.display.set_mode(size)


pygame.display.set_caption("My clickable pygame board :)")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

player = 1


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
                mousePressed(x, y, player)
                player = 2 if player == 1 else 1
                print(player)

    writePlayer(player, screen)
    drawBoard()

    pygame.display.flip()


pygame.quit()
