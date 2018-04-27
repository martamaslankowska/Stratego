import pygame
from drawing import *
from variables import *
import copy


# Initialize the game engine
pygame.init()

# Loop until the user clicks the close button.
done_starting = False
done_playing = False
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


def two_player_game(done_playing, sec_counter, ses_time, previous_time, countdown, count_color_text, count_color_back):
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
                    field = game.field_color_change(x, y, board_margin)
                    if field is not None:
                        game.field_and_player_change(field)
                        ses_time = copy.copy(session_time + 1)

        # COUNTDOWN COUNTING
        if previous_time == 0 and ses_time == (session_time + 1) and sec_counter == 28:
            game.session_time_expired()

        # BOARD DRAWING
        draw_panel_line()
        draw_board()

        # COUNTDOWN DRAWING
        count_color_text, count_color_back = countdown_color_change(countdown, count_color_text, count_color_back)
        draw_countdown(count_color_back)
        text_countdown(countdown, count_color_text)

        # PANEL DRAWING
        ap, s = text_plain()
        draw_players(ap, s)

        pygame.display.flip()

    pygame.quit()



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
                field = game.field_color_change(x, y, board_margin)
                if field is not None:
                    game.field_and_player_change(field)
                    ses_time = copy.copy(session_time + 1)

    # COUNTDOWN COUNTING
    if previous_time == 0 and ses_time == (session_time + 1) and sec_counter == 28:
        game.session_time_expired()

    # BOARD DRAWING
    draw_panel_line()
    draw_board()

    # COUNTDOWN DRAWING
    count_color_text, count_color_back = countdown_color_change(countdown, count_color_text, count_color_back)
    draw_countdown(count_color_back)
    text_countdown(countdown, count_color_text)

    # PANEL DRAWING
    ap, s = text_plain()
    draw_players(ap, s)

    pygame.display.flip()

screen.fill(WHITE)


# two_player_game(done, sec_counter, ses_time, previous_time, countdown, count_color_text, count_color_back)
