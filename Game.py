WHITE = (255, 255, 255)


class Game:

    def __init__(self, matrix, player1, player2):
        self.matrix = matrix
        self.players = [player1, player2]
        self.n = len(self.matrix)
        self.field_size = self.matrix[0][0].field_size
        self.active_player = self.players[0]
        self.next_player = self.players[1]

    def change_active_player(self):
        self.next_player = self.active_player
        self.active_player = self.players[(self.players.index(self.next_player)+1)%2]
        return self.active_player

    def count_score(self, field):
        scored = 0
        fields_lr, fields_ud, fields_lurd, fields_ruld = [], [], [], []

        ''' Checking from left to right '''
        for i in range(self.n):
            if self.matrix[field.i][i].color != WHITE:
                fields_lr.append(self.matrix[field.i][i])
        if len(fields_lr) == self.n:
            scored += self.count_line(field, fields_lr)

        ''' Checking from up to down '''
        for i in range(self.n):
            if self.matrix[i][field.j].color != WHITE:
                fields_ud.append(self.matrix[i][field.j])
        if len(fields_ud) == self.n:
            scored += self.count_line(field, fields_ud)

        fx, fy = field.i, field.j

        ''' Checking from left-up to right-down '''
        tmp_x, tmp_y = fx, fy
        for i in range(field.n_lu):
            tmp_x, tmp_y = tmp_x - 1, tmp_y - 1
            if self.matrix[tmp_x][tmp_y].color != WHITE:
                fields_lurd = [self.matrix[tmp_x][tmp_y]] + fields_lurd
        fields_lurd.append(field)
        tmp_x, tmp_y = fx, fy
        for i in range(field.n_rd):
            tmp_x, tmp_y = tmp_x + 1, tmp_y + 1
            if self.matrix[tmp_x][tmp_y].color != WHITE:
                fields_lurd.append(self.matrix[tmp_x][tmp_y])

        if len(fields_lurd) == (field.n_lu + 1 + field.n_rd):
            scored += self.count_line(field, fields_lurd)

        ''' Checking from right-up to left-down '''
        tmp_x, tmp_y = fx, fy
        for i in range(field.n_ld):
            tmp_x, tmp_y = tmp_x - 1, tmp_y + 1
            if self.matrix[tmp_x][tmp_y].color != WHITE:
                fields_ruld = [self.matrix[tmp_x][tmp_y]] + fields_ruld
        fields_ruld.append(field)
        tmp_x, tmp_y = fx, fy
        for i in range(field.n_ru):
            tmp_x, tmp_y = tmp_x + 1, tmp_y - 1
            if self.matrix[tmp_x][tmp_y].color != WHITE:
                fields_ruld.append(self.matrix[tmp_x][tmp_y])

        if len(fields_ruld) == (field.n_ru + 1 + field.n_ld):
            scored += self.count_line(field, fields_ruld)

        # print('For field ({0},{1}) - {2} and {3} | {4} and {5}'.
        #       format(field.i, field.j, count_line(field, fields_lr), count_line(field, fields_ud), count_line(field, fields_lurd), count_line(field, fields_ruld)))
        return scored

    def count_line(self, field, fields):
        a, z, x = fields.index(field), fields.index(field), fields.index(field)
        score = 0
        while a > 0:
            a -= 1
            if fields[a].color == field.color:
                score += 1
            else:
                a = 0

        while z < (len(fields) - 1):
            z += 1
            if fields[z].color == field.color:
                score += 1
            else:
                z = (len(fields) - 1)

        return score + 1 if score > 0 else 0

    def field_color_change(self, mouseX, mouseY, board_margin):
        if board_margin < mouseX < (self.n * self.field_size + board_margin) and board_margin < mouseY < (
                self.n * self.field_size + board_margin):
            field = self.matrix[int((mouseX - board_margin) / self.field_size)][int((mouseY - board_margin) / self.field_size)]
            if field.color == WHITE and self.active_player is not None:
                field.color = self.active_player.color
                return field

    def field_and_player_change(self, field):
        self.active_player.score += self.count_score(field)
        self.change_active_player()

    def session_time_expired(self):
        self.active_player = self.next_player
        self.next_player = self.players[(self.players.index(self.next_player) + 1) % 2]
