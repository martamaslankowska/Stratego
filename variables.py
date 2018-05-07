import pygame
from Game import *
from Player import *
from Field import *

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
GRAY = (128, 128, 128)

LIGHTGRAY = (183, 183, 183)
DARKGRAY = (91, 91, 91)
COLORP1 = (30, 144, 255)
COLORP1_LIGHT = (0, 191, 255)
COLORP2 = (255, 75, 165)
COLORP2_LIGHT = (255, 128, 190)

# Colors for players to pick :)
BLUE = (0, 128, 255)
BLUE_LIGHT = (77, 166, 255)
RED = (179, 0, 0)
RED_LIGHT = (255, 26, 26)
PINK = (230, 0, 115)
PINK_LIGHT = (255, 77, 166)
ORANGE = (255, 102, 0)
ORANGE_LIGHT = (255, 133, 51)
YELLOW = (255, 204, 0)
YELLOW_LIGHT = (255, 214, 51)
GREEN = (0, 204, 0)
GREEN_LIGHT = (51, 255, 51)
SEE = (0, 204, 153)
SEE_LIGHT = (51, 255, 204)

''' Used variables '''
n = 3
field_size = 70
panel_size = 400, 350
matrix = init_matrix(n, field_size)
board_margin = int(field_size/2)

pygame.init()

width, height = screen_size()
screen = pygame.display.set_mode([width, height])
# screen = pygame.display.get_surface()
pygame.display.set_icon(pygame.image.load("images.png"))

# countdown
font_semibold_60 = pygame.font.SysFont("Lato Semibold", 60)
countdown_color_text = BLACK
countdown_color_background = GRAY

font_semibold_36 = pygame.font.SysFont("Lato Semibold", 36)
font_semibold_30 = pygame.font.SysFont("Lato Semibold", 30)
font_semibold_24 = pygame.font.SysFont("Lato Semibold", 24)
font_30 = pygame.font.SysFont("Lato", 30)
font_bold_30 = pygame.font.SysFont("Lato Black", 30)
font_bold_48 = pygame.font.SysFont("Lato Black", 48)
font_semibold_48 = pygame.font.SysFont("Lato Semibold", 48)


''' Game variables '''

# player1 = Player("Marta", COLORP1, 0)
player1 = ComputerPlayer("Laptop", COLORP1, 0)
# player2 = Player("Basia", COLORP2, 1)
player2 = ComputerPlayer("Computer", COLORP2, 1)

session_time = 30

game = Game(matrix, player1, player2)
