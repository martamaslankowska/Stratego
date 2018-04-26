import pygame
from drawing import *
from variables import *
import copy


# Initialize the game engine
pygame.init()

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

pygame.display.set_caption("STRATEGO - logic game")

# Countdown variables
countdown = copy.copy(session_time)
ses_time = copy.copy(session_time)
count_color_text = copy.copy(countdown_color_text)
count_color_back = copy.copy(countdown_color_background)


while not done:

    # This limits the while loop to a max of n times per second.
    clock.tick(20)
    screen.fill(WHITE)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.USEREVENT:
            ses_time, countdown = watch_session_time(ses_time)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                field = field_change(x, y)
                if field is not None:
                    count_score(field)

    draw_panel_line()
    draw_board()

    count_color_text, count_color_back = countdown_color_change(countdown, count_color_text, count_color_back)
    print(count_color_text, count_color_back)
    draw_countdown(count_color_back)
    text_countdown(countdown, count_color_text)

    # writePlayer(player, screen)
    # drawBoard()

    pygame.display.flip()


pygame.quit()
