import pygame
from variables import *
from drawing import *
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

screen = pygame.display.set_mode([width, height])


while not done:

    # This limits the while loop to a max of n times per second.
    clock.tick(30)
    sec_counter += 1
    screen.fill(WHITE)

    ''' COMPUTER MOVE '''

    if type(game.active_player) is ComputerPlayer and game.empty_fields_nr > 0:
        computer_player = game.active_player
        winning_game_state = computer_player.decision(copy.deepcopy(game), computer_player, 4)
        print('\n---------------------------------------\nScore difference:', winning_game_state.count_computer_score())
        field = computer_player.get_changed_field(game, winning_game_state)
        print('Computer pick: (', field.i, ',', field.j, ')\n---------------------------------------\n')
        game.matrix[field.i][field.j].color = computer_player.color
        game.field_and_player_change(game.matrix[field.i][field.j])

        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j].print_short()


    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.USEREVENT:
            if game.empty_fields_nr > 0:
                previous_time = ses_time
                ses_time, countdown = watch_session_time(ses_time, game.active_player)
                sec_counter = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                field = game.field_color_change(x, y, board_margin)
                if field is not None:
                    game.field_and_player_change(field)
                    ses_time = copy.copy(session_time + 1)

                    # game.print_matrix()

                    # substates = [f.matrix for f in game.players[1].possible_children_states(copy.deepcopy(game), game.active_player)]
                    # for sub in substates:
                        # print('\n---------------------\n')
                        # for s in sub:
                        #     for f in s:
                        #         f.print_short()
                        #     # f.print_cords()

                    # states = game.players[1].possible_children_states(copy.deepcopy(game), game.active_player)
                    # for s in states:
                    #     print('Player 1:', s.players[0].score, ' |  Player 2:', s.players[1].score)
                        # print('Score difference -', s.count_active_player_score_diff(game.active_player), '\n')

                    # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nEMPTY FIELDS\n')
                    # for ef in game.empty_fields:
                    #     ef.print_short()
                    # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')



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

    if game.empty_fields_nr == 0:
        draw_finishing_box()

    pygame.display.flip()

pygame.quit()