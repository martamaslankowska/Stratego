import pygame
from variables import *
from Game import *


def draw_panel_line():
    pygame.draw.line(screen, BLACK, [width-panel_size[0], int(field_size/4)], [width-panel_size[0], height - int(field_size/4)])


def draw_board():
    for i in range(n):
        for j in range(n):
            field = matrix[i][j]
            pygame.draw.rect(screen, field.color, [field.x_left, field.y_up, field_size, field_size])
            pygame.draw.rect(screen, BLACK, [field.x_left, field.y_up, field_size, field_size], 2)


def fieldClick(mouseX, mouseY):
    field = matrix[int((mouseX - board_margin) / field_size)][int((mouseY - board_margin) / field_size)]
    field.color = game.active_player.color
    game.change_active_player()
    field.print_cords()
    field.print_neighbours()












def draw_something():
    pygame.draw.rect(screen, BLACK, [0,0,50,50])

