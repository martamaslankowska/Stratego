class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0


class ComputerPlayer(Player):
    def __init__(self):
        super(Player)

    def min_max(self):
        pass

    def alpha_betha(self):
        pass
