import copy
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


    def min_max(self):
        pass

    def alpha_betha(self):
        pass


    def possible_children_states(self, current_game, active_player):
        list_of_states = []
        for f in current_game.empty_fields:
            i, j = f.i, f.j
            game_state = copy.deepcopy(current_game)
            field = game_state.matrix[i][j]

            # print('All fields:', [item for sublist in game_state.matrix for item in sublist])
            # field.print_short()
            # print(game_state.active_player)

            game_state.active_player = game_state.players[active_player.nr]
            game_state.active_player.copy_player(active_player.name, active_player.color, active_player.nr, active_player.score)
            # print('State active players:', game_state.active_player)
            # print('State players:', game_state.players)
            field.color = game_state.active_player.color
            game_state.field_and_player_change(field)
            list_of_states.append(game_state)
            # for i in range(game_state.n):
            #     for j in range(game_state.n):
            #         game_state.matrix[i][j].print_short()

            # for i in range(game_state.n):
            #     for j in range(game_state.n):
            #         game_state.matrix[i][j].print_short()

            # field.print_short()
            # print('Player score after this move:', game_state.count_active_player_score_diff(active_player), '\n')

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
                return max([self.minimax(x, next_player, depth-1) for x in children])
            else:
                return min([self.minimax(x, next_player, depth-1) for x in children])

    def decision(self, game_state, active_player, depth=10):
        children, next_player = self.possible_children_states(game_state, active_player)
        best = max(children, key=lambda x: self.minimax(x, next_player, depth))
        for i in range(len(children)):
            f = self.get_changed_field(game_state, children[i])
            print('Children with field ({0}, {1}) - best score: {2}'.format(f.i, f.j, children[i].count_computer_score()))
        return best

    def get_changed_field(self, game, game_state):
        for i in range(game.n):
            for j in range(game.n):
                if game.matrix[i][j].color != game_state.matrix[i][j].color:
                    return game.matrix[i][j]

