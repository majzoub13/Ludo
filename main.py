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
        self.state = State()

        self.protected = [0, 47, 13, 8, 26, 21, 39, 34]
        for p in self.protected:
            self.state.board[p].protected(True)

    def main(self):

        play = self.logic.move(self.state.board, self.state.base, self.Player1,self.state.safe)
        i = 0
        while i < 100:
            print(self.state)
            if play == 1:
                play = self.logic.move(self.state.board, self.state.base, self.Player1,self.state.safe)
            else:
                play = self.logic.move(self.state.board, self.state.base, self.Player2,self.state.safe)
            print(self.state)
            i += 1


if __name__ == "__main__":
    Main().main()
