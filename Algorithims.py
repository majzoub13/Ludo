from Player import Player
import copy


class Algorithims:
    from Logic import Logic

    logic = Logic()

    # outout is the next best possible state
    def expectimax(self, state, depth, max_player, min_player, number):

        if depth == 0:
            return state
        # Determine if the current player is maximizing or minimizing
        player = state.curr_player
        turn = player.turn
        is_maximizing = turn == 1
        best_value = float("-inf") if is_maximizing else float("inf")
        best_state = state  # Keep track of the best state
        # Generate all possible states based on the current dice roll
        curr_state=copy.deepcopy(state)
        all_states = self.all_possible_states(curr_state, number)

        for new_state in all_states:
            expected_value = 0
            for dice_roll in range(1, 7):
                temp_state=copy.deepcopy(new_state)
                future_state = self.expectimax(
                    temp_state, depth - 1, min_player, max_player, dice_roll
                )
                expected_value += future_state.score * (
                    1 / 6
                )  # khalil (future_state.score * (1 / 6)* dice_roll)

            if is_maximizing:
                if expected_value > best_value:
                    best_value = expected_value
                    best_state = new_state
            else:
                if expected_value < best_value:
                    best_value = expected_value
                    best_state = new_state

        return best_state

    def all_possible_states(self, state, number):
        states = []
        player = state.curr_player
        if number != 6 and len(player.get_movable_pieces()) == 0:
            return []
        if number == 6:
            if not player.is_home_empty():
                new_state = copy.deepcopy(state)
                self.logic.add_piece(new_state.board, player)
                states.append(new_state)
        for piece in player.get_movable_pieces():
            new_state = copy.deepcopy(state)
            self.logic.check_and_move(new_state,piece, number,0)
            states.append(new_state)
        print(states)
        return states

    def evaluate_state(self, state, number):
        new_state = copy.deepcopy(state)
        logic.check_and_move(new_state.board, piece, number,0)
        return new_state
