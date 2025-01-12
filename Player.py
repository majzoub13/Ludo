class Player:
    def __init__(self, turn):
        self.turn = turn
        self.pieces = []

    def place_piece(self, index, position):
        self.pieces[index] = position
