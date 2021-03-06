import pygame
pygame.init()
from variables import *
from Game import *
import copy


''' DRAW BOARD AND PANEL 
    draw_panel_line()
    draw_board()
    text_plain()
    draw_players()
    draw_active_player()
    draw_finishing_box()
'''


def draw_panel_line():
    pygame.draw.line(screen, BLACK, [width-panel_size[0], int(field_size/4)], [width-panel_size[0], height - int(field_size/4)])


def draw_board():
    for i in range(n):
        for j in range(n):
            field = matrix[i][j]
            pygame.draw.rect(screen, field.color, [field.x_left, field.y_up, field_size, field_size])
            pygame.draw.rect(screen, BLACK, [field.x_left, field.y_up, field_size, field_size], 2)


def text_plain(move):
    txt = font_semibold_30.render("Active player", True, BLACK)
    pos = width - panel_size[0] + 55, board_margin + 110 - move
    screen.blit(txt, pos)
    score = font_semibold_30.render("Score", True, BLACK)
    pos_score = width - 45 - score.get_rect().centerx*2 - 17, board_margin + 110 - move
    screen.blit(score, pos_score)
    # pygame.draw.line(screen, GRAY, [width - 45 - score.get_rect().centerx*2 - 34, board_margin + 117],
    #                  [width - 45 - score.get_rect().centerx*2 - 34, board_margin + 142], 2)
    return txt, score


def draw_players(txt, score, move=0):
    pygame.draw.rect(screen, COLORP1_LIGHT, [width - panel_size[0] + 45, board_margin + 158 - move, panel_size[0]-90, 50])
    pygame.draw.rect(screen, COLORP2_LIGHT, [width - panel_size[0] + 45, board_margin + 215 - move, panel_size[0]-90, 50])

    # PLAYER NAMES
    pl1 = font_30.render(game.players[0].name, True, BLACK)
    pos1 = width - panel_size[0] + 55 + txt.get_rect().centerx - pl1.get_rect().centerx, board_margin + 163 - move
    pl2 = font_30.render(game.players[1].name, True, BLACK)
    pos2 = width - panel_size[0] + 55 + txt.get_rect().centerx - pl2.get_rect().centerx, board_margin + 220 - move

    pygame.draw.line(screen, COLORP1, [width - 45 - score.get_rect().centerx * 2 - 34, board_margin + 165 - move],
                     [width - 45 - score.get_rect().centerx * 2 - 34, board_margin + 201 - move], 2)
    pygame.draw.line(screen, COLORP2, [width - 45 - score.get_rect().centerx * 2 - 34, board_margin + 222 - move],
                     [width - 45 - score.get_rect().centerx * 2 - 34, board_margin + 258 - move], 2)

    # PLAYER SCORES
    pl1_score = font_30.render(str(game.players[0].score), True, BLACK)
    pos1_score = width - 45 - score.get_rect().centerx*2 - 17 + score.get_rect().centerx - pl1_score.get_rect().centerx, board_margin + 163 - move
    pl2_score = font_30.render(str(game.players[1].score), True, BLACK)
    pos2_score = width - 45 - score.get_rect().centerx*2 - 17 + score.get_rect().centerx - pl2_score.get_rect().centerx, board_margin + 220 - move

    pl1, pl2, pl1_score, pl2_score = draw_active_player(pl1, pl2, pl1_score, pl2_score)

    screen.blit(pl1, pos1)
    screen.blit(pl2, pos2)
    screen.blit(pl1_score, pos1_score)
    screen.blit(pl2_score, pos2_score)


def draw_active_player(pl1, pl2, pl1_s, pl2_s):
    if game.active_player == game.players[0]:
        pl1 = font_bold_30.render(game.players[0].name, True, BLACK)
        pl1_s = font_bold_30.render(str(game.players[0].score), True, BLACK)
    if game.active_player == game.players[1]:
        pl2 = font_bold_30.render(game.players[1].name, True, BLACK)
        pl2_s = font_bold_30.render(str(game.players[1].score), True, BLACK)
    return pl1, pl2, pl1_s, pl2_s


def draw_finishing_box():
    background = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    background.fill((255, 255, 255, 150))
    screen.blit(background, (0, 0))

    local_width, local_height = 420, 200
    local_x, local_y = int(width / 2) - int(local_width/2), int(height / 2) - int(local_height/2)

    box = pygame.Rect(local_x, local_y, local_width, local_height)
    pygame.draw.rect(screen, (180, 180, 180), box)
    pygame.draw.rect(screen, (90, 90, 90), box, 5)

    winner_text = ' wins!'
    if game.players[0].score > game.players[1].score:
        winner_text = game.players[0].name + winner_text
    elif game.players[1].score > game.players[0].score:
        winner_text = game.players[1].name + winner_text
    else:
        winner_text = 'We have a tie :)'
    score_text = str(game.players[0].score) + ' : ' + str(game.players[1].score) \
        if game.players[0].score > game.players[1].score else str(game.players[1].score) + ' : ' + str(game.players[0].score)

    winner = font_bold_48.render(winner_text, True, BLACK)
    score = font_semibold_48.render(score_text, True, BLACK)

    screen.blit(winner, (local_x + int(local_width/2) - int(winner.get_rect().width/2), local_y + 35))
    screen.blit(score, (local_x + int(local_width/2) - int(score.get_rect().width/2), local_y+100))


def draw_colors_to_pick():
    pass


def pick_a_color(active_p1, active_p2):
    pass


''' COUNTDOWN (SESSION TIME) 
    watch_session_time()
    text_countdown()
    draw_countdown()
    countdown_color_change()
'''


def watch_session_time(ses_time, last_active_player):
    ses_time -= 1
    countdown = ses_time if ses_time > 0 else 0
    if ses_time == -1:
        ses_time = copy.copy(session_time) + 1
    if ses_time <= 0:
        game.active_player = None
    return ses_time, countdown


def text_countdown(sec, color):
    countdown = font_semibold_60.render(str(sec), True, color)
    pos = width - int(panel_size[0]/2)-5 if sec < 10 else width - int(panel_size[0]/2)-25, board_margin
    screen.blit(countdown, pos)


def draw_countdown(color):
    pygame.draw.rect(screen, color, [width-panel_size[0]+75, board_margin, panel_size[0]-120, 75])
    image = pygame.image.load("hourglass.png")
    image = pygame.transform.scale(image, (58, 75))
    screen.blit(image, (width-panel_size[0]+45, board_margin))


def countdown_color_change(sec, color_text, color_back):
    if sec > 3:
        return BLACK, GRAY
    if sec > 0:
        return BLACK, (color_back[0]+2 if color_back[0]+2 < 255 else 255, color_back[1]-1 if color_back[1]-1 > 0 else 0, color_back[2]-1 if color_back[2]-1 > 0 else 0)
    else:
        return (color_text[0]+6 if color_text[0]+6 < 255 else 255, color_text[1], color_text[2]), \
               (color_back[0]+2 if color_back[0]+2 < 255 else 255, 0, 0)


