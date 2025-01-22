from Piece import Piece
import random as rand
from copy import deepcopy
from my_game import LudoScreen


class Logic:
    def __init__(self):
        self.places = [0, 13, 26, 39]
        self.color_protected_places = {"y": 0, "r": 26}
        self.baseSpot = {1: 50, -1: 24}
        self.screen = LudoScreen()
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
        if not player.is_home_empty() and self.count_pieces(player) < 4:
            home_piece = player.get_home_piece()

            home_piece.pos = self.color_protected_places[player.team]
            player.pieces[home_piece.id] = home_piece

            board[self.color_protected_places[player.team]].pieces.append(home_piece)
            return True
        return False

    def move_piece(self, state, piece, number, index):
        piece.counter += number
        # pices in safe movement
        if state.curr_player.in_safe[index]:
            curr_pos = piece.safe
            if piece.counter < 56:
                new_pos = piece.counter - 51
                if new_pos > 5:
                    print("Wrong input")
                    return curr_pos
                piece.safe = new_pos

                if piece in state.safe[state.curr_player.turn][curr_pos].pieces:
                    state.safe[state.curr_player.turn][curr_pos].pieces.remove(piece)
                state.safe[state.curr_player.turn][new_pos].pieces.append(piece)
                state.curr_player.pieces[index] = piece
                self.update_player_score(state)
                return new_pos
            elif piece.counter == 56:
                if state.curr_player.team == "r":
                    state.base.red += 1
                    if piece in state.safe[state.curr_player.turn][curr_pos].pieces:
                        state.safe[state.curr_player.turn][curr_pos].pieces.remove(
                            piece
                        )
                        piece.safe = None
                        piece.inBase = True
                        state.curr_player.pieces[index] = piece

                elif state.curr_player.team == "y":
                    state.base.yellow += 1
                    if piece in state.safe[state.curr_player.turn][curr_pos].pieces:
                        state.safe[state.curr_player.turn][curr_pos].pieces.remove(
                            piece
                        )
                        piece.safe = None
                        piece.inBase = True
                        state.curr_player.pieces[index] = piece
                else:
                    print("No addition to base yet")
            else:
                print("Can't move beyond the base")
                piece.counter -= number

                self.update_player_score(state)
                return curr_pos
        else:
            # The piece is on the board
            curr_pos = piece.pos
            if piece in state.board[curr_pos].pieces:
                state.board[curr_pos].pieces.remove(piece)
            next_pos = curr_pos + number

            # Move piece logic
            if piece.counter > 50 and piece.counter < 56:
                piece.pos = None
                new_safe_pos = piece.counter - 51
                piece.safe = new_safe_pos

                state.safe[state.curr_player.turn][new_safe_pos].pieces.append(piece)
                state.curr_player.in_safe[index] = True
                state.curr_player.pieces[index] = piece
                self.update_player_score(state)
                return new_safe_pos

            elif piece.counter == 56:
                if state.curr_player.team == "r":
                    piece.pos = None
                    state.base.red += 1
                    piece.inBase = True
                    state.curr_player.pieces[index] = piece
                elif state.curr_player.team == "y":
                    piece.pos = None
                    state.base.yellow += 1
                    piece.inBase = True
                    state.curr_player.pieces[index] = piece
                else:
                    print("No addition to base yet")
            else:
                # Calculate the next position
                if next_pos >= 51:
                    next_pos -= 51
                piece.pos = next_pos
                state.board[next_pos].pieces.append(piece)
                state.curr_player.pieces[index] = piece
                self.update_player_score(state)

                return next_pos

    def move(self, state, depth=0,number=None,selected_piece_id=None):
        # if win state exit
        if self.check_win(state.base):
            return state
        # roll dice
        if number is None:
            number = self.roll_dice()
        print(state.curr_player)
        print("dice roll:", number)
        # for three sixes only
        if depth == 4:
            new_state = deepcopy(state)
            self.change_player(new_state)
            return new_state

        if state.curr_player.turn == 1:
            # we have all pieces in home(starting case)
            if (
                state.curr_player.all_pieces_in_home()
                or len(state.curr_player.get_movable_pieces()) == 0
            ):
                new_state = deepcopy(state)
                if number == 6:
                    if self.add_piece(new_state.board, new_state.curr_player):
                        self.update_player_score(new_state)

                        print(new_state)
                        self.screen.draw(new_state)
                        return self.move(new_state, depth + 1)
                    else:
                        print("..........problem........")
                else:
                    self.change_player(new_state)
                    return new_state

            # if we have pieces in home not placed
            if not state.curr_player.is_home_empty():
                if selected_piece_id is not None:
                    piece = state.curr_player.pieces[selected_piece_id]
                    # Implement logic to move the selected piece using the dice result
                    if self.check_and_move(new_state, piece, number, selected_piece_id):
                        # Move the piece and update the state
                        self.update_player_score(new_state)
                        print(new_state)
                        self.screen.draw(new_state)
                        return new_state
                if number == 6:
                    while True:
                        try:
                            choice = int(
                                input("Choose 0 to add a new piece or 1 to move piece\n")
                            )
                            match choice:
                                case 0:
                                    new_state = deepcopy(state)
                                    self.add_piece(new_state.board, new_state.curr_player)
                                    self.update_player_score(new_state)

                                    print(new_state)
                                    self.screen.draw(new_state)
                                    return self.move(new_state, depth + 1)
                                case 1:
                                    # we have move case outside for both states when base is empty
                                    # and when there is in base but we want to move
                                    # pass
                                    break
                                case _:
                                    continue
                                    # print("You're not supposed to be here")
                                    # return state
                        except:
                            continue

            # if the player home is empty and we need to move only or for move
            pieces = state.curr_player.get_movable_pieces()
            new_state = deepcopy(state)
            if len(pieces) == 1:
                if number == 6:
                    if self.check_and_move(new_state, pieces[0], number, pieces[0].id)[1]:
                        newer_state = deepcopy(new_state)
                        self.move(newer_state, depth)

                    print(new_state)
                    self.screen.draw(new_state)
                    return self.move(new_state, depth + 1)
                else:
                    if self.check_and_move(new_state, pieces[0], number, pieces[0].id)[1]:
                        newer_state = deepcopy(new_state)
                        self.move(newer_state, depth)

                    self.change_player(new_state)
                    self.screen.draw(new_state)
                    print(new_state)
                    return new_state

            print("Choose piece to move")
            indexes = []
            for index, piece in enumerate(pieces):
                if not piece.inBase:
                    if piece.safe is not None:
                        if number + piece.safe >= 6:
                            continue
                        print(f"{piece.id}- piece at safe position: {piece.safe}")
                    else:
                        # Todo if wall state dont show for the user
                        print(f"{piece.id}- piece at board position: {piece.pos}")
                    indexes.append(piece.id)

            while True:
                try:
                    user_choice = int(
                        input("Enter the id of the piece you want to select (0-3): ")
                    )
                    # input validation
                    if not user_choice in indexes:
                        continue

                    piece = state.curr_player.pieces[user_choice]
                    if number == 6:
                        if self.check_and_move(new_state, piece, number, user_choice)[1]:
                            newer_state = deepcopy(new_state)
                            self.move(newer_state, depth)

                        print(new_state)
                        self.screen.draw(new_state)
                        return self.move(new_state, depth + 1)
                    else:
                        if self.check_and_move(new_state, piece, number, user_choice)[1]:
                            newer_state = deepcopy(new_state)
                            self.move(newer_state, depth)

                        self.change_player(new_state)
                        self.screen.draw(new_state)
                        print(new_state)
                        return new_state
                except:
                    continue
        # computer turn
        else:
            if state.curr_player.all_pieces_in_home():
                new_state = deepcopy(state)
                if number == 6:
                    self.add_piece(new_state.board, new_state.curr_player)
                    self.update_player_score(new_state)

                    print(new_state)
                    self.screen.draw(new_state)
                    return self.move(new_state, depth + 1)
                else:
                    self.change_player(new_state)
                    return new_state
            else:
                from Algorithims import Algorithims

                algo = Algorithims()

                new_state = algo.expectimax(
                    state, 2, state.players[0], state.players[1], number
                )
                self.update_player_score(new_state)

                if number == 6:
                    print(new_state)
                    self.screen.draw(new_state)
                    return self.move(new_state, depth + 1)

                else:
                    self.change_player(new_state)
                    self.screen.draw(new_state)
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

    def check_and_move(self, state, piece, number, choice):
        if piece.inBase or piece.counter + number > 56:
            return (False, False)

        if piece.pos is None and piece.safe is None:
            return (False, False)

        print(f"GG {piece.id}: POS:{piece.pos} SAFE:{piece.safe}")

        if (
            piece.safe is not None
            and len(state.safe[state.curr_player.turn][piece.safe].pieces) > 0
            and piece in state.safe[state.curr_player.turn][piece.safe].pieces
        ):
            self.move_piece(
                state,
                piece,
                number,
                choice,
            )
            return (True, False)

        if piece.pos is None:
            return (False, False)

        current_pos = piece.pos
        potential_pos = current_pos + number

        # checking if the potential index has pieces
        # if it doesn't we check for wall
        if potential_pos >= 51:
            potential_pos -= 51

        if (len(state.board[potential_pos].pieces) == 0) or (
            len(state.board[potential_pos].pieces) > 0
            and state.board[potential_pos].pieces[0].team == piece.team
        ):
            if potential_pos > current_pos:
                for i in range(current_pos + 1, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(state.board[i].pieces) > 1
                        and state.board[i].pieces[0] != None
                        and state.board[i].pieces[0].team != piece.team
                    ):
                        return (False, False)
                # here the path is clear so we move
                self.move_piece(
                    state,
                    piece,
                    number,
                    choice,
                )
                return (True, False)
            else:
                for i in range(current_pos, 52):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(state.board[i].pieces) > 1
                        and state.board[i].pieces[0] != None
                        and state.board[i].pieces[0].team != piece.team
                    ):
                        return (False, False)

                for i in range(0, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(state.board[i].pieces) > 1
                        and state.board[i].pieces[0] != None
                        and state.board[i].pieces[0].team != piece.team
                    ):
                        return (False, False)
                # here the path is clear so we move
                self.move_piece(
                    state,
                    piece,
                    number,
                    choice,
                )
                return (True, False)

        # if it does we try to kill/remove the piece
        else:
            for p in state.board[potential_pos].pieces:
                if p.team != piece.team and not state.board[potential_pos].is_protected:
                    self.kill(state.board, potential_pos)
                    self.move_piece(
                        state,
                        piece,
                        number,
                        choice,
                    )
                    return (True, True)
            return (False, False)

    def kill(self, board, position):
        for piece in board[position].pieces:
            board[position].pieces.remove(piece)
            piece.pos = None
        return

    def get_score(self, state):
        score = 0
        for p in state.players:
            score += p.score * p.turn
        return score

    def update_player_score(self, state):
        for p in state.players:
            p.score = 0
            for piece in p.pieces:
                if piece.pos == None:
                    p.score -= 5
                else:
                    p.score += piece.counter
                    if state.board[piece.pos].is_protected:
                        p.score += 5

    def count_pieces(self, player):
        return len(
            [
                piece
                for piece in player.pieces
                if piece.pos is not None or piece.safe is not None
            ]
        )
