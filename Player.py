from Piece import Piece


class Player:
    def __init__(self, turn, team):
        self.turn = turn
        self.team = team
        self.pieces = [
            Piece(team),
            Piece(team),
            Piece(team),
            Piece(team),
        ]

    def place_piece(self, index, position):
        self.pieces[index] = position

    def get_home_piece(self):
        for piece in self.pieces:
            if piece.pos is None:
                return piece

    def get_movable_pieces(self):
        movable_pieces = [piece for piece in self.pieces if piece.pos is not None]
        print(movable_pieces)
        return movable_pieces

    def is_home_empty(self):
        return not any(piece.pos is None for piece in self.pieces)

    def all_pieces_in_home(self):
        return all(piece.pos is None for piece in self.pieces)

    def __str__(self):
        return f"Player Team: {self.team} Turn: {self.turn}"
