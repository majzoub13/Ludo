from State import State
from Player import Player
from Piece import Piece
from LudoNode import Node
from Logic import Logic
import random as rand


class Main:
    def __init__(self):
        self.logic = Logic()
        self.Player1 = Player(1)
        self.Player2 = Player(-1)
        self.protected = [0, 47, 13, 8, 26, 21, 39, 34]

        nodes = [Node() for _ in range(52)]
        self.state = State(nodes)

        for p in self.protected:
            self.state.board[p] = Node(True)

    def main(self):

        play = self.logic.move(self.state.board, self.state.base, self.Player1)
        i = 0
        while i < 20:
            print(self.state)
            if play == 1:
                play = self.logic.move(self.state.board, self.state.base, self.Player1)
            else:
                play = self.logic.move(self.state.board, self.state.base, self.Player2)
            print(self.state)
            i += 1


if __name__ == "__main__":
    Main().main()
