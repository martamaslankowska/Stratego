import pygame
from drawing import *
from variables import *
import copy


# Initialize the game engine
pygame.init()

# Loop until the user clicks the close button.
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


def starting_screen():
    sw, sh = 500, 400
    loc_screen = pygame.display.set_mode((sw, sh))
    font_p1, font_p2 = font_30, font_30
    p1_input_box = pygame.Rect(loc_screen.get_rect().centerx - 100, 140, 200, 45)
    p2_input_box = pygame.Rect(loc_screen.get_rect().centerx - 100, 200, 200, 45)

    clock = pygame.time.Clock()

    color_inactive_p1 = COLORP1_LIGHT
    color_active_p1 = COLORP1
    color_p1 = color_inactive_p1
    color_inactive_p2 = COLORP2_LIGHT
    color_active_p2 = COLORP2
    color_p2 = color_inactive_p2

    active_p1 = False
    active_p2 = False
    text_p1, text_p2 = '', ''

    text = 'Enter player names and play!'
    text_button = 'start game'
    button = pygame.Rect(loc_screen.get_rect().centerx - 85, 300, 170, 50)
    draw_line = False

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if p1_input_box.collidepoint(event.pos):
                    # Toggle the active_p1 variable.
                    active_p1 = not active_p1
                    active_p2 = False if active_p1 else True
                else:
                    active_p1 = False

                if p2_input_box.collidepoint(event.pos):
                    # Toggle the active_p1 variable.
                    active_p2 = not active_p2
                    active_p1 = False if active_p2 else True
                else:
                    active_p2 = False

                # Change the current color of the input box.
                color_p1 = color_active_p1 if active_p1 else color_inactive_p1
                font_p1 = font_semibold_30 if active_p1 else font_30

                color_p2 = color_active_p2 if active_p2 else color_inactive_p2
                font_p2 = font_semibold_30 if active_p2 else font_30

                if button.collidepoint(event.pos):
                    if text_p1 == '' or text_p2 == '':
                        draw_line = True
                    else:
                        done = True

            if event.type == pygame.KEYDOWN:
                if active_p1:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        text_p1 = text_p1[:-1]
                    else:
                        text_p1 += event.unicode
                if active_p2:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        text_p2 = text_p2[:-1]
                    else:
                        text_p2 += event.unicode

                if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                    if text_p1 == '' or text_p2 == '':
                        draw_line = True
                    else:
                        done = True

        loc_screen.fill(WHITE)

        # Main text
        txt = font_semibold_30.render(text, True, BLACK)
        txt_button = font_semibold_24.render(text_button, True, BLACK)

        # Render the current text.
        txt_p1 = font_p1.render(text_p1, True, color_p1)
        txt_p2 = font_p2.render(text_p2, True, color_p2)

        # Resize the box if the text is too long.
        p1_width = max(200, txt_p1.get_width() + 30)
        p2_width = max(200, txt_p2.get_width() + 30)

        p1_input_box = pygame.Rect(loc_screen.get_rect().centerx - int(p1_width / 2), 140, p1_width, 45)
        p2_input_box = pygame.Rect(loc_screen.get_rect().centerx - int(p2_width / 2), 200, p2_width, 45)

        # Blit the text_p1.
        loc_screen.blit(txt_p1, (p1_input_box.centerx - int(txt_p1.get_rect().width / 2), p1_input_box.y + 5))
        loc_screen.blit(txt_p2, (p2_input_box.centerx - int(txt_p2.get_rect().width / 2), p2_input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(loc_screen, color_p1, p1_input_box, 4 if active_p1 else 2)
        pygame.draw.rect(loc_screen, color_p2, p2_input_box, 4 if active_p2 else 2)

        # Blit button
        pygame.draw.rect(loc_screen, GRAY, button)
        pygame.draw.rect(loc_screen, BLACK, button, 2)
        loc_screen.blit(txt_button, (button.centerx - int(txt_button.get_rect().width / 2), 310))
        # Blit the main text
        loc_screen.blit(txt, (int(sw / 2) - int(txt.get_rect().width / 2), 50))
        if draw_line:
            pygame.draw.line(loc_screen, BLACK, [(int(sw / 2) - int(txt.get_rect().width / 2) - 5), 90],
                             [(int(sw / 2) - int(txt.get_rect().width / 2) + 257), 90], 3)

        pygame.display.flip()
        clock.tick(30)

    return text_p1, text_p2


def two_player_game(done, sec_counter, ses_time, previous_time, countdown, count_color_text, count_color_back):
    screen = pygame.display.set_mode([width, height])

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
                if game.empty_fields_left > 0:
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

        if game.empty_fields_left == 0:
            draw_finishing_box()

        pygame.display.flip()

    pygame.quit()



# p1_name, p2_name = starting_screen()
# if p1_name == '' or p2_name == '':
#     done_playing = True
# else:
#     game.players[0].name, game.players[1].name = p1_name, p2_name

two_player_game(done_playing, sec_counter, ses_time, previous_time, countdown, count_color_text, count_color_back)


