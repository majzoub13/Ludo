from State import State
from Player import Player
from Piece import Piece
from LudoNode import Node
from Logic import Logic
import random as rand


class Main:
    def __init__(self):
        self.logic = Logic()
        self.Player1 = Player(1, "y")
        self.Player2 = Player(-1, "r")
        self.init_state = State([self.Player1, self.Player2])

        self.protected = [0, 47, 13, 8, 26, 21, 39, 34]
        for p in self.protected:
            self.init_state.board[p].protected(True)

    def main(self):
        new_state = self.logic.move(self.init_state, 1)
        i = 0
        while i < 20:
            new_state = self.logic.move(new_state, 1)
            i += 1


if __name__ == "__main__":
    Main().main()
