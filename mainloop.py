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
previous_time = ses_time
count_color_text = copy.copy(countdown_color_text)
count_color_back = copy.copy(countdown_color_background)
sec_counter = 0


while not done:

    # This limits the while loop to a max of n times per second.
    clock.tick(30)
    sec_counter += 1
    screen.fill(WHITE)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.USEREVENT:
            previous_time = ses_time
            ses_time, countdown = watch_session_time(ses_time, game.active_player)
            sec_counter = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                field = field_change(x, y)
                if field is not None:
                    game.active_player.score += count_score(field)
                    game.change_active_player()
                    ses_time = copy.copy(session_time+1)

    if previous_time == 0 and ses_time == (session_time+1) and sec_counter == 28:
        game.active_player = game.next_player
        game.next_player = game.players[(game.players.index(game.next_player) + 1) % 2]

    draw_panel_line()
    draw_board()

    count_color_text, count_color_back = countdown_color_change(countdown, count_color_text, count_color_back)
    draw_countdown(count_color_back)
    text_countdown(countdown, count_color_text)

    ap, s = text_plain()
    draw_players(ap, s)

    # writePlayer(player, screen)
    # drawBoard()

    pygame.display.flip()


pygame.quit()
