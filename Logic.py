from Piece import Piece
import random as rand


class Logic:
    def __init__(self):
        self.places = [0, 13, 26, 39]
        self.color_protected_places = {"y": 0, "r": 26}
        self.baseSpot = {1:50, -1:24}
        return

    def roll_dice(self):
        return rand.randint(1, 6)

    def add_piece(self, board, player):
        home_piece = player.get_home_piece()
        board[self.color_protected_places[player.team]].pieces.append(home_piece)
        home_piece.pos = self.color_protected_places[player.team]
        print(home_piece.pos)
        # if player.turn == 1:
        #     board[self.places[0]].pieces.append(Piece("y"))
        #     player.pieces.append(self.places[0])
        #     print(f"player pieces is {player.pieces}")
        # elif player.turn == -1:
        #     board[self.places[2]].pieces.append(Piece("r"))
        #     player.pieces.append(self.places[2])
        # else:
        #     return

    def move_piece(self, board, curr_pos, piece, number, player, safe, index):
        if piece in board[curr_pos].pieces:
            board[curr_pos].pieces.remove(piece)
        next_pos = curr_pos + number

        if next_pos >= (len(board) - 1):
            next_pos = next_pos - len(board) - 1
        if self.baseSpot[player.turn] in list(range(curr_pos, next_pos)):
            piece.counter += number
            safe[player.turn][self.baseSpot[player.turn]-next_pos].pieces.append(piece)
            player.pieces[index] = self.baseSpot[player.turn]-next_pos
            return self.baseSpot[player.turn]-next_pos
        piece.counter += number
        board[next_pos].pieces.append(piece)
        player.pieces[index] = next_pos
        piece.pos = next_pos
        return next_pos

    def move(self, board, base, player,safe ,depth=0):
        if self.check_win(base):
            print(self.check_win(base) + "won")
            return

        number = self.roll_dice()
        print(player)
        print("dice roll:", number)
        if depth == 4:
            return

        if player.turn == 1:
            # we have all pieces in base(starting case)
            if player.all_pieces_in_home():
                if number == 6:
                    self.add_piece(board, player)
                    self.move(board, base, player, depth + 1)
                    return
                else:
                    return

            # if we have pieces in base not placed
            if not player.is_home_empty():
                print(f"GG{number}")
                if number == 6:
                    choice = int(
                        input("Choose 0 to add a new piece or 1 to move piece")
                    )
                    match choice:
                        case 0:
                            self.add_piece(board, player)
                            self.move(board, base, player, depth + 1)
                            return
                        case 1:
                            # we have move case outside for both states when base is empty and when there is in base but we want to move
                            pass
                        case _:
                            print("you're not supposed to be here")
                            return

            # if the player base is empty and we need to move only or for move
            pieces = player.get_movable_pieces()
            print("choose piece to move")
            for index, piece in enumerate(pieces):
                print(f"{index}- piece at {piece.pos}")
            user_choice = int(
                input("Enter the index of the piece you want to select (0-4): ")
            )
            # need to implement check if input validation
            piece = pieces[user_choice]
            if number == 6:
                self.check_and_move(board, player, piece, number)
                self.move(board, base, player, depth + 1)
            else:
                self.check_and_move(board, player, piece, number)
                return

            # if len(player.pieces) == 0:
            #     if number == 6:
            #         self.add_piece(board, player)
            #         return 1
            #     else:
            #         return -1
            # else:
            #     if number == 6:
            #         choice = int(
            #             input("Choose 0 to add a new piece or 1 to move piece\n")
            #         )
            #         match choice:
            #             case 0:
            #                 self.add_piece(board, player)
            #                 return 1
            #             case 1:
            #                 print("Choose piece to move")

            #                 indexes = []
            #                 for index, piece in enumerate(player.pieces):
            #                     indexes.append(index)
            #                     print(f"for piece at position {piece}: enter {index}\n")
            #                 ans = int(input())

            #                 if ans in indexes:
            #                     pos = self.move_piece(board, piece, number, player, safe, ans)
            #                     player.pieces[index] = pos
            #                     return -1
            #             case default:
            #                 return "error"
            #     else:
            #         print("Choose piece to move")

            #         indexes = []
            #                 ghassan = []
            #         for index, piece in enumerate(player.pieces):
            #             indexes.append(index)
            #                     ghassan.append(piece)
            #             print(f"for piece at position {piece}: enter {index}\n")
            #         ans = int(input())

            #         if ans in indexes:
            #             pos = self.move_piece(board, ghassan[ans], number,player,safe,ans)
            #             player.pieces[index] = pos
            #             return -1
        else:
            number = self.roll_dice()
            if len(player.pieces) == 0:
                if number == 6:
                    self.add_piece(board, player)
                    return -1
                else:
                    return 1
            else:
                if number == 6:
                    self.add_piece(board, player)
                    return -1
                else:
                    indexes = []
                    ghassan=[]
                    print(player.pieces)
                    for index, piece in enumerate(player.pieces):
                        indexes.append(index)
                        ghassan.append(piece)
                        print(f"for piece at position {piece}: enter {index}\n")
                    ans = rand.choice(indexes)
                    print(indexes)
                    print(ans)
                    if ans in indexes:
                        pos = self.move_piece(board, ghassan[ans], number,player,safe,ans)
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

    def check_and_move(self, board, player, piece, number):
        current_pos = piece.pos
        potential_pos = current_pos + number
        # checking if the potential index has pieces
        # if it doesn't we check for wall
        if potential_pos > 51:
            potential_pos -= 51

        if (
            len(board[potential_pos].pieces) > 0
            and board[potential_pos].pieces[0].team == piece.team
        ):
            self.move_piece(board, current_pos, piece, number)
            return

        if len(board[potential_pos].pieces) == 0:
            if potential_pos > current_pos:
                for i in range(current_pos + 1, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors and different from the moved piece team
                    if (
                        len(board[i].pieces)
                        and len(board[i].pieces) > 1
                        and board[i].pieces[0] != None
                        and board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(board, current_pos, piece, number)
            else:
                for i in range(current_pos, 52):
                    # checked that two pieces of the same team excluding None are neighbors and different from the moved piece team
                    if (
                        len(board[i].pieces)
                        and len(board[i].pieces) > 1
                        and board[i].pieces[0] != None
                        and board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(board, current_pos, piece, number)
                for i in range(0, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors and different from the moved piece team
                    if (
                        len(board[i].pieces)
                        and len(board[i].pieces) > 1
                        and board[i].pieces[0] != None
                        and board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(board, current_pos, piece, number)
        # if it does we try to kill/remove the piece
        else:
            for p in board[potential_pos].pieces:
                if p.team != piece.team:
                    self.kill(board, potential_pos)
                    return True

    def kill(self, board, position):
        for piece in board[position].pieces:
            piece.position = None
            board[position].pieces.remove(piece)
            return
