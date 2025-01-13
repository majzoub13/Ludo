from Piece import Piece
import random as rand


class Logic:
    def __init__(self):
        self.places = [0, 13, 26, 39]
        return

    def roll_dice(self):
        return rand.randint(1, 6)

    def add_piece(self, board, player):
        if player.turn == 1:
            board[self.places[0]].pieces.append(Piece("y"))
            player.pieces.append(self.places[0])
            print(f"player pieces is {player.pieces}")
        elif player.turn == -1:
            board[self.places[2]].pieces.append(Piece("r"))
            player.pieces.append(self.places[2])
        else:
            return

    def move_piece(self, board, curr_pos, number):
        piece = board[curr_pos].pieces.pop()
        next_pos = curr_pos + number
        piece.counter += number
        board[next_pos].pieces.append(piece)
        return next_pos

    def move(self, board, base, player, depth=0):
        if self.check_win(base):
            print(self.check_win(base) + "won")
            return

        number = self.roll_dice()
        print(f"player is {player.turn}")
        print(f"you rolled {number}")
        if player.turn == 1:
            if len(player.pieces) == 0:
                if number == 6:
                    self.add_piece(board, player)
                    return 1
                else:
                    return -1
            else:
                if number == 6:
                    choice = int(
                        input("Choose 0 to add a new piece or 1 to move piece\n")
                    )
                    match choice:
                        case 0:
                            self.add_piece(board, player)
                            return 1
                        case 1:
                            print("Choose piece to move")

                            indexes = []
                            for index, piece in enumerate(player.pieces):
                                indexes.append(index)
                                print(f"for piece at position {piece}: enter {index}\n")
                            ans = int(input())

                            if ans in indexes:
                                pos = self.move_piece(board, piece, number)
                                player.pieces[index] = pos
                                return -1
                        case default:
                            return "error"
                else:
                    print("Choose piece to move")

                    indexes = []
                    for index, piece in enumerate(player.pieces):
                        indexes.append(index)
                        print(f"for piece at position {piece}: enter {index}\n")
                    ans = int(input())

                    if ans in indexes:
                        pos = self.move_piece(board, piece, number)
                        player.pieces[index] = pos
                        return -1
        else:
            number = 6
            if len(player.pieces) == 0:
                if number == 6:
                    self.add_piece(board, player)
                    return -1
                else:
                    return 1
            else:
                return 1

    def check_win(self, base):
        if base.red == 4:
            return "red"
        if base.green == 4:
            return "green"
        if base.blue == 4:
            return "blue"
        if base.yellow == 4:
            return "yellow"
        return None
