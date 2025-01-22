from Piece import Piece


class Player:
    def __init__(self, turn, team):
        self.turn = turn
        self.team = team
        self.score = 0
        self.in_safe = [
            False,
            False,
            False,
            False,
        ]
        self.pieces = [
            Piece(team, 0),
            Piece(team, 1),
            Piece(team, 2),
            Piece(team, 3),
        ]

    def place_piece(self, index, position):
        self.pieces[index] = position

    def get_movable_pieces(self):
        movable_pieces = []

        for piece in self.pieces:
            if piece.pos is not None or piece.safe is not None:
                movable_pieces.append(piece)
        return movable_pieces

    def is_home_empty(self):
        return not any(
            piece.pos is None and piece.safe is None and not piece.inBase
            for piece in self.pieces
        )

    def all_pieces_in_home(self):
        return all(
            piece.pos is None and piece.safe is None and not piece.inBase
            for piece in self.pieces
        )

    def get_home_pieces(self):
        # all pieces
        home_pieces = []
        for piece in self.pieces:
            if piece.pos is None and piece.safe is None and not piece.inBase:
                home_pieces.append(piece)
        return home_pieces

    def get_home_piece(self):
        # first None piece
        for piece in self.pieces:
            if piece.pos is None and piece.safe is None and not piece.inBase:
                return piece

    def __str__(self):
        return f"Player Team: {self.team} Turn: {self.turn}"
