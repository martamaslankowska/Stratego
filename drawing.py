import pygame
from variables import *
from Game import *
import copy


def draw_panel_line():
    pygame.draw.line(screen, BLACK, [width-panel_size[0], int(field_size/4)], [width-panel_size[0], height - int(field_size/4)])


def draw_board():
    for i in range(n):
        for j in range(n):
            field = matrix[i][j]
            pygame.draw.rect(screen, field.color, [field.x_left, field.y_up, field_size, field_size])
            pygame.draw.rect(screen, BLACK, [field.x_left, field.y_up, field_size, field_size], 2)


def field_change(mouseX, mouseY):
    if board_margin < mouseX < (n*field_size+board_margin) and board_margin < mouseY < (n*field_size+board_margin):
        field = matrix[int((mouseX - board_margin) / field_size)][int((mouseY - board_margin) / field_size)]
        if field.color == WHITE:
            field.color = game.active_player.color
            game.change_active_player()
            return field


def count_score(field):
    pass


def watch_session_time(ses_time):
    ses_time -= 1
    countdown = ses_time if ses_time > 0 else 0
    if ses_time == -2:
        game.change_active_player()
        ses_time = copy.copy(session_time) + 1
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
        return BLACK, (color_back[0]+3 if color_back[0]+3 < 255 else 255, color_back[1]-1, color_back[2]-1)
    else:
        return (color_text[0]+4, color_text[1]+4, color_text[2]+4), (color_back[0]+3 if color_back[0]+3 < 255 else 255, color_back[1]-1, color_back[2]-1)









def draw_something():
    pygame.draw.rect(screen, BLACK, [0,0,50,50])

