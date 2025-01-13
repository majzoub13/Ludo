from Piece import Piece
import random as rand


class Logic:
    def __init__(self):
        self.protected_places = [13, 39]
        self.color_protected_places = {
            "y":0
            "r":26
        }
        return

    def roll_dice(self):
        return rand.randint(1, 6)

    def add_piece(self, board, player):
            base_piece = Player.get_base_piece
            board[self.color_protected_places[player.team]].pieces.append(base_piece)
            base_piece.position = self.color_protected_places[player.team]

    def move_piece(self, board, curr_pos, number):
        piece = board[curr_pos].pieces.pop()
        next_pos = curr_pos + number
        piece.counter += number
        board[next_pos].pieces.append(piece)
        return next_pos

    def move(self, board, player, depth=0):
        if player.turn == 1:
            number = self.roll_dice()
            print(number)
            if len(player.pieces) == 0:
                if number == 6:
                    self.add_piece(board, player)
                    if player.turn == 1:
                        return 1
                    else:
                        return -1
                else:
                    if player.turn == 1:
                        return -1
                    else:
                        return 1
            else:
                if number == 6:
                    choice = input("Choose 0 to add a new piece or 1 to move piece")
                    match choice:
                        case 0:
                            self.add_piece(board, player.turn)
                            if player.turn == 1:
                                return 1
                            else:
                                return -1
                        case 1:
                            print("Choose piece to move")

                            indexes = []
                            for index, piece in enumerate(player.pieces):
                                indexes.append(index)
                                ans = input(
                                    f"for piece at position {piece}: enter {index}"
                                )

                            if ans in indexes:
                                pos = self.move_piece(board, piece, number)
                                player.pieces[index] = pos
                                if player.turn == 1:
                                    return -1
                                else:
                                    return 1
                        case default:
                            return "error"
                else:
                    print("Choose piece to move")

                    indexes = []
                    for index, piece in enumerate(player.pieces):
                        indexes.append(index)
                        ans = input(f"for piece at position {piece}: enter {index}")

                    if ans in indexes:
                        pos = self.move_piece(board, piece, number)
                        player.pieces[index] = pos
                        if player.turn == 1:
                            return -1
                        else:
                            return 1
            print(number)

        else:
            return
        
    def check_and_move(self,board,player,piece,current_index,potential_index):
        # checking if the potential index has pieces
        # if it doesn't we check for wall
        if len(board[potential_index].pieces) == 0:
            for i in range(current_index + 1, potential_index + 1):
                # checked that two pieces of the same team excluding None are neighbors and different from the moved piece team
                 if board[i].pieces[0].team == board[i+1].pieces[0].team and board[i].pieces[0] != piece.team and board[i].pieces[0] != None:
                     return False
                 # here the path is clear so we move
                 else    
                    pos = self.move_piece(board, piece, potential_index - current_index)
                    player.pieces[current_index] = pos      
        # if it does we try to kill/remove the piece 
        else:
            for p in board[potential_index].pieces:
                if p.team != piece.team:
                    kill(board,p)    
                    return True
    def kill(self,board,piece):
        board[piece.position].pieces.remove(piece)
        piece.position = None
        return
        
            
