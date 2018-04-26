from Field import *


class Game:

    def __init__(self, matrix, player1, player2):
        self.matrix = matrix
        self.players = [player1, player2]
        self.n = len(matrix)
        self.field_size = matrix[0][0].field_size
        self.active_player = self.players[0]
        self.next_player = self.players[1]


    def change_active_player(self):
        self.next_player = self.active_player
        self.active_player = self.players[(self.players.index(self.next_player)+1)%2]
        return self.active_player



    # def change_player(self, player):
    #     if player == self.players[0]:
    #         self.active_player = self.players[1]
    #     if player == self.players[1]:
    #         self.active_player = self.players[0]
    #     return self.active_player


    def points_scored(self, field):

        pass


    def line_score(self, fields):
        pass





# Game.init_matrix(8, 50)