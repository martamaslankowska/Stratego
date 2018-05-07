import copy
import sys

WHITE = (255, 255, 255)


class Player:

    def __init__(self, name, color, number):
        self.name = name
        self.color = color
        self.score = 0
        self.nr = number

    def copy_player(self, name, color, number, score):
        self.name = name
        self.color = color
        self.score = score
        self.nr = number


class ComputerPlayer(Player):
    def __init__(self, name, color, number):
        super().__init__(name, color, number)


    def possible_children_states(self, current_game, active_player):
        list_of_states = []
        for f in current_game.empty_fields:
            i, j = f.i, f.j
            game_state = copy.deepcopy(current_game)
            field = game_state.matrix[i][j]

            game_state.active_player = game_state.players[active_player.nr]
            game_state.active_player.copy_player(active_player.name, active_player.color, active_player.nr, active_player.score)

            field.color = game_state.active_player.color
            game_state.field_and_player_change(field)
            list_of_states.append(game_state)

        next_player = current_game.players[(active_player.nr+1)%2]
        return list_of_states, next_player


    def minimax(self, game_state, active_player, depth):
        if game_state.empty_fields_nr == 0:
            return game_state.count_computer_score()
        elif depth == 0:
            return game_state.count_computer_score()
        else:
            children, next_player = self.possible_children_states(game_state, active_player)
            if type(game_state.players[active_player.nr]) is ComputerPlayer:
                return min([self.minimax(x, next_player, depth-1) for x in children])
            else:
                return max([self.minimax(x, next_player, depth-1) for x in children])


    # returns computer score while playing
    def minimax_alpha_beta(self, game_state, active_player, depth, alpha, beta):
        if game_state.empty_fields_nr == 0:
            return game_state.count_computer_score()
        elif depth == 0:
            return game_state.count_computer_score()
        else:
            children, next_player = self.possible_children_states(game_state, active_player)
            if type(game_state.players[active_player.nr]) is ComputerPlayer:
                value = -sys.maxsize
                for child_state in children:
                    value = max(value,
                                self.minimax_alpha_beta(child_state, next_player, depth - 1, alpha, beta))
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        # print('There was a pruning! Beta cut off... O.O')
                        break
                return value
            else:
                value = sys.maxsize
                for child_state in children:
                    value = min(value,
                                self.minimax_alpha_beta(child_state, next_player, depth - 1, alpha, beta))
                    beta = min(beta, value)
                    if beta <= alpha:
                        # print('There was a pruning! Alpha cut off... O.O ')
                        break
                return value


    def decision_minimax(self, game_state, active_player, depth=10):
        children, next_player = self.possible_children_states(game_state, active_player)
        best = max(children, key=lambda x: self.minimax(x, next_player, depth))
        return best, children


    def decision_alpha_beta(self, game_state, active_player, depth=10):
        children, next_player = self.possible_children_states(game_state, active_player)
        best = max(children, key=lambda x: self.minimax_alpha_beta(x, next_player, depth, -sys.maxsize, sys.maxsize))
        return best, children


    def get_changed_field(self, game, game_state):
        for i in range(game.n):
            for j in range(game.n):
                if game.matrix[i][j].color != game_state.matrix[i][j].color:
                    return game.matrix[i][j]





    # returns computer score and number of prunings while playing
    # it really returns number of visited states
    def minimax_alpha_beta_statstics(self, game_state, active_player, depth, alpha, beta, prunings):
        if game_state.empty_fields_nr == 0:
            prunings += 1
            return game_state.count_computer_score(), prunings
        elif depth == 0:
            prunings += 1
            return game_state.count_computer_score(), prunings
        else:
            children, next_player = self.possible_children_states(game_state, active_player)
            if type(game_state.players[active_player.nr]) is ComputerPlayer:
                value = -sys.maxsize
                for child_state in children:
                    minimax_res, prunings = self.minimax_alpha_beta_statstics(child_state, next_player, depth-1, alpha, beta, prunings)
                    prunings += 1
                    value = max(value, minimax_res)
                    # alpha = max(alpha, value)
                    # if beta <= alpha:
                    #     print('There was a pruning! Beta cut off... O.O')
                    #     break
                return value, prunings
            else:
                value = sys.maxsize
                for child_state in children:
                    minimax_res, prunings = self.minimax_alpha_beta_statstics(child_state, next_player, depth-1, alpha, beta, prunings)
                    prunings += 1
                    value = min(value, minimax_res)
                    # beta = min(beta, value)
                    # if beta <= alpha:
                    #     print('There was a pruning! Alpha cut off... O.O')
                    #     break
                return value, prunings

    def decision_alpha_beta_statistics(self, game_state, active_player, depth=10):
        children, next_player = self.possible_children_states(game_state, active_player)
        best_value, best_child, nr_of_nodes = -sys.maxsize, children[0], 0
        for child in children:
            value, prunings = self.minimax_alpha_beta_statstics(child, next_player, depth, -sys.maxsize, sys.maxsize, 0)
            if value > best_value:
                best_value = value
                best_child = child
                nr_of_nodes += prunings
        return best_child, children, nr_of_nodes
