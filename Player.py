from Piece import Piece
class Player:
    def __init__(self, turn, team):
        self.turn = turn
        self.team = team
        self.pieces = [
            piece_1 = Piece(team,None),
            piece_2 = Piece(team,None),
            piece_3 = Piece(team,None),
            piece_4 = Piece(team,None)        
        ]
        

    def place_piece(self, index, position):
        self.pieces[index] = position
    def get_base_piece(self):
         for piece in self.pieces:
                if piece.position is None:
                    return piece
