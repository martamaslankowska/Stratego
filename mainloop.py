import pygame
from drawing import *
from variables import *


# Initialize the game engine
pygame.init()

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
pygame.display.set_caption("STRATEGO - logic game")


while not done:

    # This limits the while loop to a max of 10 times per second.
    clock.tick(10)
    screen.fill(WHITE)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                fieldClick(x, y)

                # mousePressed(x, y, player)
                # player = 2 if player == 1 else 1
                # print(player)

    draw_panel_line()
    draw_board()

    # writePlayer(player, screen)
    # drawBoard()

    pygame.display.flip()


pygame.quit()
