import copy
WHITE = (255, 255, 255)


class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0


class ComputerPlayer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)


    def min_max(self):
        pass

    def alpha_betha(self):
        pass


    def possible_children_states(self, current_game):
        list_of_states = []
        for f in current_game.empty_fields:
            game_state = copy.deepcopy(current_game)
            game_state.field_and_player_change(f)
            list_of_states.append(game_state)
        return list_of_states



    def minimax(self, game_state, depth):
        if game_state.empty_fields_nr == 0:
            return game_state
        elif depth == 0:
            return game_state
        else:
            pass
            # children = self.possible_children_states()
            # if type(game_state.active_player) is ComputerPlayer:
            #     return max([m.score for m in children])
            # else:
            #     return min([m.score for m in children])

