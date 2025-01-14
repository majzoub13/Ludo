from Piece import Piece
import random as rand
from copy import deepcopy


class Logic:
    def __init__(self):
        self.places = [0, 13, 26, 39]
        self.color_protected_places = {"y": 0, "r": 26}
        self.baseSpot = {1: 50, -1: 24}
        return

    def roll_dice(self):
        return rand.randint(1, 6)

    def change_player(self, state):
        if state.curr_player.turn == 1:
            state.curr_player = state.players[1]
        elif state.curr_player.turn == -1:
            state.curr_player = state.players[0]
        else:
            return

    def add_piece(self, board, player):
        home_piece = player.get_home_piece()
        board[self.color_protected_places[player.team]].pieces.append(home_piece)
        home_piece.pos = self.color_protected_places[player.team]

    def move_piece(self, board, piece, number, player, safe, index, base):
        curr_pos = piece.pos
        if player.in_safe[index]:
            piece.counter += number
            if piece.counter < 56:
                i = piece.counter - 50
                safe[player.turn][i].pieces.append(piece)
                player.pieces[index] = i
                return i
            elif piece.counter >= 56:
                if player.team == "r":
                    base.red += 1
                elif player.team == "y":
                    base.yellow += 1
                else:
                    pass
            else:
                print("can't move beyond the base")
                return piece.counter - number
        else:
            if piece in board[curr_pos].pieces:
                board[curr_pos].pieces.remove(piece)
            next_pos = curr_pos + number
            piece.counter += number

            if piece.counter >= 50 and piece.counter < 56:
                i = piece.counter - 50
                safe[player.turn][i].pieces.append(piece)
                player.pieces[index] = i
                return i
            elif piece.counter == 56:
                if player.team == "r":
                    base.red += 1
                elif player.team == "y":
                    base.yellow += 1
                else:
                    pass
            else:
                board[next_pos].pieces.append(piece)
                player.pieces[index] = piece
                piece.pos = next_pos
                return next_pos

    def move(self, state, depth=0):
        if self.check_win(state.base):
            print(self.check_win(state.base) + "won")
            return state

        number = self.roll_dice()
        print(state.curr_player)
        print("dice roll:", number)
        if depth == 4:
            new_state = deepcopy(state)
            self.change_player(new_state)
            return new_state

        if state.curr_player.turn == 1:
            # we have all pieces in base(starting case)
            if state.curr_player.all_pieces_in_home():
                new_state = deepcopy(state)
                if number == 6:
                    self.add_piece(new_state.board, new_state.curr_player)
                    self.update_player_score(new_state)

                    print(new_state)
                    return self.move(new_state, depth + 1)
                else:
                    self.change_player(new_state)
                    return new_state

            # if we have pieces in base not placed
            if not state.curr_player.is_home_empty():
                if number == 6:
                    choice = int(
                        input("Choose 0 to add a new piece or 1 to move piece\n")
                    )
                    match choice:
                        case 0:
                            new_state = deepcopy(state)
                            self.add_piece(new_state.board, new_state.curr_player)
                            self.update_player_score(new_state)

                            print(new_state)
                            return self.move(new_state, depth + 1)
                        case 1:
                            # we have move case outside for both states when base is empty
                            # and when there is in base but we want to move
                            pass
                        case _:
                            print("You're not supposed to be here")
                            return state

            # if the player base is empty and we need to move only or for move
            pieces = state.curr_player.get_movable_pieces()
            new_state = deepcopy(state)
            if len(pieces) == 1:
                if number == 6:
                    self.check_and_move(
                        new_state.board,
                        new_state.curr_player,
                        pieces[0],
                        number,
                        new_state.safe,
                        0,
                        state.base,
                    )
                    self.update_player_score(new_state)

                    print(new_state)
                    return self.move(new_state, depth + 1)
                else:
                    self.check_and_move(
                        new_state.board,
                        new_state.curr_player,
                        pieces[0],
                        number,
                        new_state.safe,
                        0,
                        state.base,
                    )
                    self.update_player_score(new_state)

                    self.change_player(new_state)
                    print(new_state)
                    return new_state

            print("Choose piece to move")
            for index, piece in enumerate(pieces):
                print(f"{index}- piece at position: {piece.pos}")
            user_choice = int(
                input("Enter the index of the piece you want to select (0-3): ")
            )
            # need to implement check if input validation
            piece = pieces[user_choice]
            if number == 6:
                self.check_and_move(
                    new_state.board,
                    new_state.curr_player,
                    piece,
                    number,
                    new_state.safe,
                    user_choice,
                    state.base,
                )
                self.update_player_score(new_state)

                print(new_state)
                return self.move(new_state, depth + 1)
            else:
                self.check_and_move(
                    new_state.board,
                    new_state.curr_player,
                    piece,
                    number,
                    new_state.safe,
                    user_choice,
                    state.base,
                )
                self.update_player_score(new_state)

                self.change_player(new_state)
                print(new_state)
                return new_state
        else:
            if state.curr_player.all_pieces_in_home():
                new_state = deepcopy(state)
                if number == 6:
                    self.add_piece(new_state.board, new_state.curr_player)

                    print(new_state)
                    return self.move(new_state, depth + 1)
                else:
                    self.change_player(new_state)
                    return new_state
            else:
                # if we have pieces in base not placed
                if not state.curr_player.is_home_empty():
                    if number == 6:
                        new_state = deepcopy(state)
                        self.add_piece(new_state.board, new_state.curr_player)
                        self.update_player_score(new_state)

                        print(new_state)
                        return self.move(new_state, depth + 1)

                # if the player base is empty and we need to move only or for move
                pieces = state.curr_player.get_movable_pieces()
                new_state = deepcopy(state)
                if len(pieces) == 1:
                    self.check_and_move(
                        new_state.board,
                        new_state.curr_player,
                        pieces[0],
                        number,
                        new_state.safe,
                        0,
                        state.base,
                    )
                    self.update_player_score(new_state)

                    self.change_player(new_state)
                    print(new_state)
                    return new_state

                indexes = []
                ghassan = []
                for index, piece in enumerate(pieces):
                    indexes.append(index)
                    ghassan.append(piece)
                    print(f"{index}- piece at position: {piece.pos}")
                ai_choice = rand.choice(indexes)
                # need to implement check if input validation
                piece = pieces[ai_choice]
                self.check_and_move(
                    new_state.board,
                    new_state.curr_player,
                    piece,
                    number,
                    new_state.safe,
                    ai_choice,
                    state.base,
                )
                self.update_player_score(new_state)

                self.change_player(new_state)
                print(new_state)
                return new_state

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

    def check_and_move(self, board, player, piece, number, safe, choice, base):
        current_pos = piece.pos
        potential_pos = current_pos + number
        print(f"potential_pos: {potential_pos}")
        # checking if the potential index has pieces
        # if it doesn't we check for wall
        if potential_pos > 51:
            potential_pos -= 51

        if (
            len(board[potential_pos].pieces) > 0
            and board[potential_pos].pieces[0].team == piece.team
        ):
            self.move_piece(board, piece, number, player, safe, choice, base)
            return

        if len(board[potential_pos].pieces) == 0:
            if potential_pos > current_pos:
                for i in range(current_pos + 1, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(board[i].pieces) > 1
                        and board[i].pieces[0] != None
                        and board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(
                            board, piece, number, player, safe, choice, base
                        )
                        return True
            else:
                for i in range(current_pos, 52):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(board[i].pieces) > 1
                        and board[i].pieces[0] != None
                        and board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(
                            board, piece, number, player, safe, choice, base
                        )
                        return True

                for i in range(0, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(board[i].pieces) > 1
                        and board[i].pieces[0] != None
                        and board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(
                            board, piece, number, player, safe, choice, base
                        )
                        return True

        # if it does we try to kill/remove the piece
        else:
            for p in board[potential_pos].pieces:
                if p.team != piece.team:
                    self.kill(board, potential_pos)
                    return True

    def kill(self, board, position):
        for piece in board[position].pieces:
            board[position].pieces.remove(piece)
            piece.pos = None
            return

    def update_player_score(self, state):
        player = state.curr_player
        player.score = 0
        for piece in player.pieces:
            if piece.pos == None:
                player.score -= 5
            else:
                player.score += piece.counter
                if state.board[piece.pos].is_protected:
                    player.score += 5

    def gets_score(self, state):
        score = 0
        for p in state.players:
            score += p.score * p.turn
        return score
