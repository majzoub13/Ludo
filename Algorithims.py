from Player import Player
import copy


class Algorithims:
    from Logic import Logic

    logic = Logic()

    # output is the next best possible state
    def expectimax(self, state, depth, max_player, min_player, number):

        if depth == 0 or self.logic.check_win(state.base):
            return state
        # Determine if the current player is maximizing or minimizing
        if state.curr_player.turn == 1:
            is_maximizing = True
        else:
            is_maximizing = False

        if is_maximizing:
            best_value = float("-inf")
        else:
            best_value = float("inf")
        best_state = state  # Keep track of the best state

        # Generate all possible states based on the current dice roll
        # curr_state=copy.deepcopy(state)
        all_states = self.all_possible_states(state, state.curr_player, number)
        
        if len(all_states) == 0:
            return best_state 

        for new_state in all_states:
            expected_value = 0
            for dice_roll in range(1, 7):
                temp_state = copy.deepcopy(new_state)
                future_state = self.expectimax(
                    temp_state, depth - 1, max_player, min_player, dice_roll
                )
                expected_value += future_state.score * (1 / 6)
                # khalil (future_state.score * (1 / 6)* dice_roll)

            if is_maximizing:
                if expected_value > best_value:
                    best_value = expected_value
                    best_state = copy.deepcopy(new_state)
            else:
                if expected_value < best_value:
                    best_value = expected_value
                    best_state = copy.deepcopy(new_state)
        return best_state

    def all_possible_states(self, state, player, number):
        states = []
        if number != 6 and len(player.get_movable_pieces()) == 0:
            return []
        if number == 6:
            pieces = player.get_movable_pieces()
            for index, piece in enumerate(pieces):
                new_state2 = copy.deepcopy(state)
                if self.logic.check_and_move(new_state2, piece, number, piece.id):
                    states.append(new_state2)

            if not player.is_home_empty():
                new_state1 = copy.deepcopy(state)
                if self.logic.add_piece(new_state1.board, new_state1.curr_player):
                    self.logic.update_player_score(new_state1)
                    states.append(new_state1)

        else:
            pieces = player.get_movable_pieces()
            for index, piece in enumerate(pieces):
                new_state = copy.deepcopy(state)
                if self.logic.check_and_move(new_state, piece, number, piece.id):
                    states.append(new_state)
            print(f"states fetched are {len(states)}")
        return states
