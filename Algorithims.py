from Player import Player
import copy
class Algorithims:
    # outout is the next best possible state
    def expectimax(self, state, depth, player):
        turn = player.turn
        if depth == 0 or self.terminal(state):
            return self.utility(state)

        if turn:
            bestValue = float('-inf')
            for action in self.actions(state):
                value = self.expectimax(self.result(state, action), depth - 1, False)
                bestValue = max(bestValue, value)
            return bestValue
        else:
            expectedValue = 0
            totalProbability = 0
            for outcome, probability in self.outcomes():
                value = self.expectimax(self.result(state, outcome), depth - 1, True)
                expectedValue += probability * value
                totalProbability += probability
            
            return expectedValue / totalProbability
    def all_possible_states(self,state,player,number);
        states = []
        if number == 6 :
            if not player.is_home_empty():
                new_state = 
            
