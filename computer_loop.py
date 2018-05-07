import pygame
from variables import *
from drawing import *
import copy
import time
import math
import random

# Initialize the game engine
pygame.init()

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

pygame.display.set_caption("STRATEGO - logic game")
screen = pygame.display.set_mode([width, height])

list_of_times = []
t = 0


''' ONE GAME :) '''


def single_minimax_play(screen, t):
    global done
    ended = False

    while not done:

        # This limits the while loop to a max of n times per second.
        clock.tick(30)
        screen.fill(WHITE)

        ''' COMPUTER MOVE '''
        if type(game.active_player) is ComputerPlayer and game.empty_fields_nr > 0:
            start = time.time()
            depth = game.get_depth()
            nr_of_operations = int(
                math.factorial(game.empty_fields_nr) / math.factorial(game.empty_fields_nr - (depth + 1))) \
                if game.empty_fields_nr > (depth + 1) else math.factorial(game.empty_fields_nr)

            computer_player = game.active_player
            winning_game_state, c = computer_player.decision_minimax(copy.deepcopy(game), computer_player, depth)

            if depth < 2:
                winning_game_state = game.smart_random_field(c)

            field = computer_player.get_changed_field(game, winning_game_state)
            game.matrix[field.i][field.j].color = computer_player.color
            game.field_and_player_change(game.matrix[field.i][field.j])

            end = time.time()
            t += round(end - start, 3)
            list_of_times.append(
                str(round(end - start, 3)) + '\n' + str(nr_of_operations) + '\n' + str(depth + 1) + '\n')


        # ''' RANDOM PLAYER '''
        # if type(game.active_player) is not ComputerPlayer and game.empty_fields_nr > 0:
        #     f = random.choice(game.empty_fields)
        #     field = game.field_color_change(int((f.x_left + f.x_right) / 2), int((f.y_up + f.y_down) / 2), board_margin)
        #     game.field_and_player_change(field)


        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    field = game.field_color_change(x, y, board_margin)
                    if field is not None:
                        game.field_and_player_change(field)

        # BOARD DRAWING
        draw_panel_line()
        draw_board()

        # PANEL DRAWING
        ap, s = text_plain(110)
        draw_players(ap, s, 110)

        # Finishing the game
        if ended:
            time.sleep(3)
            done = True

        if game.empty_fields_nr == 0:
            draw_finishing_box()
            ended = True

        pygame.display.flip()


def single_alpha_beta_play(screen, t):
    global done
    ended = False

    while not done:

        # This limits the while loop to a max of n times per second.
        clock.tick(30)
        screen.fill(WHITE)

        ''' COMPUTER MOVE '''
        if type(game.active_player) is ComputerPlayer and game.empty_fields_nr > 0:
            start = time.time()
            depth = game.get_depth()
            nr_of_operations = int(
                math.factorial(game.empty_fields_nr) / math.factorial(game.empty_fields_nr - (depth + 1))) \
                if game.empty_fields_nr > (depth + 1) else math.factorial(game.empty_fields_nr)

            computer_player = game.active_player
            winning_game_state, c = computer_player.decision_alpha_beta(copy.deepcopy(game), computer_player, depth)

            if depth < 2:
                winning_game_state = game.smart_random_field(c)

            field = computer_player.get_changed_field(game, winning_game_state)
            game.matrix[field.i][field.j].color = computer_player.color
            game.field_and_player_change(game.matrix[field.i][field.j])

            end = time.time()
            t += round(end - start, 3)
            list_of_times.append(
                str(round(end - start, 3)) + '\n' + str(nr_of_operations) + '\n' + str(depth + 1) + '\n')

        # ''' RANDOM PLAYER '''
        # if type(game.active_player) is not ComputerPlayer and game.empty_fields_nr > 0:
        #     f = random.choice(game.empty_fields)
        #     field = game.field_color_change(int((f.x_left + f.x_right) / 2), int((f.y_up + f.y_down) / 2), board_margin)
        #     game.field_and_player_change(field)

        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    field = game.field_color_change(x, y, board_margin)
                    if field is not None:
                        game.field_and_player_change(field)

        # BOARD DRAWING
        draw_panel_line()
        draw_board()

        # PANEL DRAWING
        ap, s = text_plain(110)
        draw_players(ap, s, 110)

        # Finishing the game
        if ended:
            time.sleep(3)
            done = True

        if game.empty_fields_nr == 0:
            draw_finishing_box()
            ended = True

        pygame.display.flip()


def single_alpha_beta_play_statistics(screen, t):
    global done
    ended = False

    while not done:

        # This limits the while loop to a max of n times per second.
        clock.tick(30)
        screen.fill(WHITE)

        ''' COMPUTER MOVE '''
        if type(game.active_player) is ComputerPlayer and game.empty_fields_nr > 0:
            start = time.time()
            depth = game.get_depth()
            nr_of_operations = int(
                math.factorial(game.empty_fields_nr) / math.factorial(game.empty_fields_nr - (depth + 1))) \
                if game.empty_fields_nr > (depth + 1) else math.factorial(game.empty_fields_nr)

            computer_player = game.active_player
            winning_game_state, c, nodes = computer_player.decision_alpha_beta_statistics(copy.deepcopy(game), computer_player, depth)

            print('\nNodes:', nodes, '(having', game.empty_fields_nr, 'fields)')

            if depth < 2:
                winning_game_state = game.smart_random_field(c)

            field = computer_player.get_changed_field(game, winning_game_state)
            game.matrix[field.i][field.j].color = computer_player.color
            game.field_and_player_change(game.matrix[field.i][field.j])

            end = time.time()
            t += round(end - start, 3)
            list_of_times.append(
                str(round(end - start, 3)) + '\n' + str(nr_of_operations) + '\n' + str(depth + 1) + '\n')

        # ''' RANDOM PLAYER '''
        # if type(game.active_player) is not ComputerPlayer and game.empty_fields_nr > 0:
        #     f = random.choice(game.empty_fields)
        #     field = game.field_color_change(int((f.x_left + f.x_right) / 2), int((f.y_up + f.y_down) / 2), board_margin)
        #     game.field_and_player_change(field)

        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    field = game.field_color_change(x, y, board_margin)
                    if field is not None:
                        game.field_and_player_change(field)

        # BOARD DRAWING
        draw_panel_line()
        draw_board()

        # PANEL DRAWING
        ap, s = text_plain(110)
        draw_players(ap, s, 110)

        # Finishing the game
        if ended:
            time.sleep(3)
            done = True

        if game.empty_fields_nr == 0:
            draw_finishing_box()
            ended = True

        pygame.display.flip()



def file_save_minimax_statistics(screen):
    for matrix_dim in range(3, 5):
        n = matrix_dim
        for nr in range(3):

            ''' INITIALIZE NEW GAME '''
            done = False
            matrix = init_matrix(n, field_size)
            player1 = Player("Marta", COLORP1, 0)
            player2 = ComputerPlayer("Comp", COLORP2, 1)
            game = Game(matrix, player1, player2)

            ''' FILE SAVE - time and statistics'''
            file_name = 'times_n' + (('0' + str(matrix_dim)) if matrix_dim < 10 else str(matrix_dim)) \
                        + '_nr' + (('0' + str(nr)) if nr < 10 else str(nr)) + '.txt'
            list_of_times = []
            t = 0

            while not done:

                # This limits the while loop to a max of n times per second.
                clock.tick(30)
                screen.fill(WHITE)

                ''' COMPUTER MOVE '''
                if type(game.active_player) is ComputerPlayer and game.empty_fields_nr > 0:
                    start = time.time()
                    depth = game.get_depth()
                    nr_of_operations = int(math.factorial(game.empty_fields_nr) / math.factorial(game.empty_fields_nr - (depth+1))) \
                        if game.empty_fields_nr > (depth+1) else math.factorial(game.empty_fields_nr)

                    computer_player = game.active_player
                    winning_game_state, c = computer_player.decision_minimax(copy.deepcopy(game), computer_player, depth)

                    if depth < 2:
                        winning_game_state = game.smart_random_field(c)

                    field = computer_player.get_changed_field(game, winning_game_state)
                    game.matrix[field.i][field.j].color = computer_player.color
                    game.field_and_player_change(game.matrix[field.i][field.j])

                    end = time.time()
                    t += round(end - start, 3)
                    list_of_times.append(str(round(end - start, 3)) + '\n' + str(nr_of_operations) + '\n' + str(depth+1) + '\n')



                ''' RANDOM PLAYER '''
                if type(game.active_player) is not ComputerPlayer and game.empty_fields_nr > 0:
                    f = random.choice(game.empty_fields)
                    field = game.field_color_change(int((f.x_left+f.x_right)/2), int((f.y_up+f.y_down)/2), board_margin)
                    game.field_and_player_change(field)



                x, y = pygame.mouse.get_pos()

                for event in pygame.event.get():  # User did something
                    if event.type == pygame.QUIT:  # If user clicked close
                        done = True  # Flag that we are done so we exit this loop

                    # if event.type == pygame.MOUSEBUTTONDOWN:
                    #     if event.button == 1:
                    #         field = game.field_color_change(x, y, board_margin)
                    #         if field is not None:
                    #             game.field_and_player_change(field)

                # BOARD DRAWING
                draw_panel_line()
                draw_board()

                # PANEL DRAWING
                ap, s = text_plain(110)
                draw_players(ap, s, 110)

                if game.empty_fields_nr == 0:
                    draw_finishing_box()
                    done = True

                pygame.display.flip()

            list_of_times.append(str(round(t,3)) + '\n')
            list_of_times.append(str(game.players[0].score) + '\n' + str(game.players[1].score))

            with open(file_name, 'w') as file:
                for i in list_of_times:
                    file.write(i)


def file_save_alpha_beta_statistics(screen):
    for matrix_dim in range(8, 12):
        n = matrix_dim
        for nr in range(5):

            ''' INITIALIZE NEW GAME '''
            done = False
            matrix = init_matrix(n, field_size)
            player1 = Player("Marta", COLORP1, 0)
            player2 = ComputerPlayer("Comp", COLORP2, 1)
            game = Game(matrix, player1, player2)

            ''' FILE SAVE - time and statistics'''
            file_name = 'times_ab_n' + (('0' + str(matrix_dim)) if matrix_dim < 10 else str(matrix_dim)) \
                        + '_nr' + (('0' + str(nr)) if nr < 10 else str(nr)) + '.txt'
            list_of_times = []
            t = 0

            while not done:

                # This limits the while loop to a max of n times per second.
                clock.tick(30)
                screen.fill(WHITE)

                ''' COMPUTER MOVE '''
                if type(game.active_player) is ComputerPlayer and game.empty_fields_nr > 0:
                    start = time.time()
                    depth = game.get_depth()
                    nr_of_operations = int(math.factorial(game.empty_fields_nr) / math.factorial(game.empty_fields_nr - (depth+1))) \
                        if game.empty_fields_nr > (depth+1) else math.factorial(game.empty_fields_nr)

                    computer_player = game.active_player
                    winning_game_state, c = computer_player.decision_alpha_beta(copy.deepcopy(game), computer_player, depth)

                    if depth < 2:
                        winning_game_state = game.smart_random_field(c)

                    field = computer_player.get_changed_field(game, winning_game_state)
                    game.matrix[field.i][field.j].color = computer_player.color
                    game.field_and_player_change(game.matrix[field.i][field.j])

                    end = time.time()
                    t += round(end - start, 3)
                    list_of_times.append(str(round(end - start, 3)) + '\n' + str(nr_of_operations) + '\n' + str(depth+1) + '\n')



                ''' RANDOM PLAYER '''
                if type(game.active_player) is not ComputerPlayer and game.empty_fields_nr > 0:
                    f = random.choice(game.empty_fields)
                    field = game.field_color_change(int((f.x_left+f.x_right)/2), int((f.y_up+f.y_down)/2), board_margin)
                    game.field_and_player_change(field)



                x, y = pygame.mouse.get_pos()

                for event in pygame.event.get():  # User did something
                    if event.type == pygame.QUIT:  # If user clicked close
                        done = True  # Flag that we are done so we exit this loop

                    # if event.type == pygame.MOUSEBUTTONDOWN:
                    #     if event.button == 1:
                    #         field = game.field_color_change(x, y, board_margin)
                    #         if field is not None:
                    #             game.field_and_player_change(field)

                # BOARD DRAWING
                draw_panel_line()
                draw_board()

                # PANEL DRAWING
                ap, s = text_plain(110)
                draw_players(ap, s, 110)

                if game.empty_fields_nr == 0:
                    draw_finishing_box()
                    done = True

                pygame.display.flip()

            list_of_times.append(str(round(t,3)) + '\n')
            list_of_times.append(str(game.players[0].score) + '\n' + str(game.players[1].score))

            with open(file_name, 'w') as file:
                for i in list_of_times:
                    file.write(i)


# single_minimax_play(screen, t)
single_alpha_beta_play(screen, t)
# single_alpha_beta_play_statistics(screen, t)

pygame.quit()