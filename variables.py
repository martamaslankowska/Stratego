import pygame
from Game import *
from Player import *

''' Main python file in which all variables will be set '''
''' Used methods '''


def screen_size():
    x = (n+1) * field_size + panel_size[0]
    y = (n+1) * field_size
    if y < panel_size[1]:
        y = panel_size[1]
    return x, y


def init_matrix(n, field_size):
    matrix = [[Field()] * n for a in range(n)]
    board_margin = int(field_size/2)
    for i in range(n):
        for j in range(n):
            matrix[j][i] = Field(j, i, board_margin + field_size*j, board_margin + field_size*i, field_size,
                                 j, (n-1)-j, i, (n-1)-i, min(j, i), min((n-1)-j, (n-1)-i), min((n-1)-j, i), min(j, (n-1)-i))
            # matrix[i][j].print_cords()
    return matrix


''' Colors '''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


''' Used variables '''
n = 6
field_size = 70
panel_size = 350, 250
matrix = init_matrix(n, field_size)
board_margin = int(field_size/2)

width, height = screen_size()
screen = pygame.display.set_mode([width, height])
pygame.display.set_icon(pygame.image.load("images.png"))

player1 = Player("Marta", RED)
player2 = Player("Basia", BLUE)

game = Game(matrix, player1, player2)




