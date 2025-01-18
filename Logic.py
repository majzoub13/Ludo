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
        if not player.is_home_empty() and self.count_pieces(player) < 4:
            home_piece = player.get_home_piece()
            board[self.color_protected_places[player.team]].pieces.append(home_piece)
            player.pieces[home_piece.id].pos = self.color_protected_places[player.team]
            return True
        return False

    def move_piece(self, state, piece, number, index):
        piece.counter += number
        #print(f"the counter for piece is {piece.counter}")
        # pices in safe movement
        if state.curr_player.in_safe[index]:
            curr_pos = piece.safe
            if piece.counter < 56:
                new_pos = piece.counter - 51
                if new_pos > 5:
                    return curr_pos
                piece.safe = new_pos
                if piece in state.safe[state.curr_player.turn]:
                    state.safe[state.curr_player.turn].remove(piece)
                state.safe[state.curr_player.turn][new_pos].pieces.append(piece)
                state.curr_player.pieces[index] = piece
                self.update_player_score(state)
                print(f"score for state is {self.get_score(state)}")
                return new_pos
            elif piece.counter == 56:
                if state.curr_player.team == "r":
                    state.base.red += 1
                    if piece in state.safe[curr_pos].pieces:
                        state.safe[curr_pos].pieces.remove(piece)
                        state.curr_player.pieces.pop(index)
                elif state.curr_player.team == "y":
                    state.base.yellow += 1
                    if piece in state.safe[curr_pos].pieces:
                        state.safe[curr_pos].pieces.remove(piece)
                        state.curr_player.pieces.pop(index)
                else:
                    print("no addition to base yet")
            else:
                print("can't move beyond the base")
                piece.counter -= number
                self.update_player_score(state)
                print(f"score for state is {self.get_score(state)}")
                return piece.counter
        else:
            # The piece is on the board
            curr_pos = piece.pos
            if piece in state.board[curr_pos].pieces:
                state.board[curr_pos].pieces.remove(piece)
            next_pos = curr_pos + number

            # Calculate the next position
            if next_pos >= 51:
                next_pos -= 51

            # Move piece logic
            if piece.counter > 50 and piece.counter < 56:
                piece.pos = None
                new_safe_pos = piece.counter - 51
                piece.safe = new_safe_pos
                print(f"the new index in the safe is{new_safe_pos}")
                state.safe[state.curr_player.turn][new_safe_pos].pieces.append(piece)
                state.curr_player.pieces[index] = piece
                self.update_player_score(state)
                print(f"score for state is {self.get_score(state)}")
                return new_safe_pos
            elif piece.counter == 56:
                if state.curr_player.team == "r":
                    state.base.red += 1
                    state.curr_player.pieces.pop(index)
                elif state.curr_player.team == "y":
                    state.base.yellow += 1
                    state.curr_player.pieces.pop(index)
                else:
                    print("no addition to base yet")
            else:
                #print(next_pos)
                piece.pos = next_pos
                state.board[next_pos].pieces.append(piece)
                state.curr_player.pieces[index] = piece
                self.update_player_score(state)
                print(f"score for state is {self.get_score(state)}")
                if piece.counter > 56:
                    piece.counter -= number
                return next_pos

    def move(self, state, depth=0):
        # if win state exit
        if self.check_win(state.base):
            print(self.check_win(state.base) + "won")
            return state
        # roll dice
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
            if state.curr_player.all_pieces_in_home():
                new_state = deepcopy(state)
                if number == 6:
                    if(self.add_piece(new_state.board, new_state.curr_player)):
                        self.update_player_score(new_state)
                        # print(f"score for state is {self.get_score(state)}")

                        # print(new_state)
                        return self.move(new_state, depth + 1)
                    else:
                        print("..........problem........")
                else:
                    self.change_player(new_state)
                    return new_state

            # if we have pieces in home not placed
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
                            # print(f"score for state is {self.get_score(state)}")

                            # print(new_state)
                            return self.move(new_state, depth + 1)
                        case 1:
                            # we have move case outside for both states when base is empty
                            # and when there is in base but we want to move
                            pass
                        case _:
                            print("You're not supposed to be here")
                            return state

            # if the player home is empty and we need to move only or for move
            pieces = state.curr_player.get_movable_pieces()
            new_state = deepcopy(state)
            if len(pieces) == 1:
                if number == 6:
                    self.check_and_move(new_state, pieces[0], number, 0)

                    print(new_state)
                    return self.move(new_state, depth + 1)
                else:
                    self.check_and_move(new_state, pieces[0], number, 0)

                    self.change_player(new_state)
                    print(new_state)
                    return new_state

            print("Choose piece to move")
            for index, piece in enumerate(pieces):
                if piece.safe != None:
                    if number+piece.safe>6:
                        continue
                    print(f"{piece.id}- piece at safe position: {piece.safe}")
                else:
                    # if wall state dont show for the user still n
                    if  (len(state.board[piece.pos+number].pieces) > 0
                            and state.board[piece.pos+number].pieces[0].team != piece.team):
                        continue
                    print(f"{piece.id}- piece at board position: {piece.pos}")
            user_choice = int(
                input("Enter the id of the piece you want to select (0-3): ")
            )
            # need to implement check if input validation
            piece = state.curr_player.pieces[user_choice]
            if number == 6:
                self.check_and_move(new_state, piece, number, user_choice)

                print(new_state)
                return self.move(new_state, depth + 1)
            else:
                self.check_and_move(new_state, piece, number, user_choice)

                self.change_player(new_state)
                print(new_state)
                return new_state
        #computer turn
        else:
            if state.curr_player.all_pieces_in_home():
                new_state = deepcopy(state)
                if number == 6:
                    self.add_piece(new_state.board, new_state.curr_player)
                    self.update_player_score(new_state)
                    # print(f"score for state is {self.get_score(state)}")

                    # print(new_state)
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

    def check_and_move(self, state ,piece, number, choice):
        if (
            piece.safe != None
            and len(state.safe[state.curr_player.turn][piece.safe].pieces) > 0
            and piece in state.safe[state.curr_player.turn][piece.safe].pieces
        ):
            self.move_piece(
                state,
                piece,
                number,
                choice,
            )
            return True
        current_pos = piece.pos
        potential_pos = current_pos + number
        #print(f"potential_pos: {potential_pos}")
        # checking if the potential index has pieces
        # if it doesn't we check for wall
        if potential_pos > 51:
            potential_pos -= 51
        #print(f"potential_pos: {potential_pos}")

        if (
            len(state.board[potential_pos].pieces) > 0
            and state.board[potential_pos].pieces[0].team == piece.team
        ):
            self.move_piece(
                state,
                piece,
                number,
                choice,
            )
            return True

        if len(state.board[potential_pos].pieces) == 0:
            if potential_pos > current_pos:
                for i in range(current_pos + 1, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(state.board[i].pieces) > 1
                        and state.board[i].pieces[0] != None
                        and state.board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(
                            state,
                            piece,
                            number,
                            choice,
                        )
                        return True
            else:
                for i in range(current_pos, 52):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(state.board[i].pieces) > 1
                        and state.board[i].pieces[0] != None
                        and state.board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(
                            state,
                            piece,
                            number,
                            choice,
                        )
                        return True

                for i in range(0, potential_pos + 1):
                    # checked that two pieces of the same team excluding None are neighbors
                    # and different from the moved piece team
                    if (
                        len(state.board[i].pieces) > 1
                        and state.board[i].pieces[0] != None
                        and state.board[i].pieces[0].team != piece.team
                    ):
                        return False
                    # here the path is clear so we move
                    else:
                        self.move_piece(
                            state,
                            piece,
                            number,
                            choice,
                        )
                        return True

        # if it does we try to kill/remove the piece
        else:
            for p in state.board[potential_pos].pieces:
                if p.team != piece.team and not state.board[potential_pos].is_protected:
                    self.kill(state.board, potential_pos)
                    return True
            return False

    def kill(self, board, position):
        for piece in board[position].pieces:
            board[position].pieces.remove(piece)
            piece.pos = None
        return

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

    def get_score(self, state):
        score = 0
        for p in state.players:
            print(f"player score is {p.score} for player {p.turn}")
            score += p.score * p.turn
        return score
    def count_pieces(self, player):
        return len([piece for piece in player.pieces if piece.pos is not None or piece.safe is not None])
