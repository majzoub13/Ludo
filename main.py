from State import State
from Player import Player
from Piece import Piece
from LudoNode import Node
from Logic import Logic
import random as rand
from my_game import LudoScreen
import pygame


class Main:
    def __init__(self):
        pygame.init()
        self.logic = Logic()
        self.Player1 = Player(1, "y")
        self.Player2 = Player(-1, "r")
        self.init_state = State([self.Player1, self.Player2])

        self.protected = [0, 47, 13, 8, 26, 21, 39, 34]
        for p in self.protected:
            self.init_state.board[p].protected(True)

        self.screen = LudoScreen()
        self.screen.draw(self.init_state)

    def main(self):
        new_state = self.logic.move(self.init_state, 1)

        run = True
        while run:
            win = self.logic.check_win(new_state.base)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # row, col = get_row_col_from_mouse(pos)
                    # game.select(row, col)
                    # game.update()

            if win is not None:
                print(win + " won")
                run = False
                break

            # commented this line for game not to crach and load for ever
            # new_state = self.logic.move(new_state, 1)
        pygame.quit()


if __name__ == "__main__":
    Main().main()
