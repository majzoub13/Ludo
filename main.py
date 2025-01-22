from State import State
from Player import Player
from Piece import Piece
from LudoNode import Node
from Logic import Logic
import random as rand
from my_game import LudoScreen
import pygame
from copy import deepcopy


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
        self.dice_result = None

    def main(self):
        new_state = deepcopy(self.init_state)
        print("new_state3:", new_state)
        selected_piece_id = None
        run = True
        while run:
            # Check if game ended
            win = self.logic.check_win(new_state.base)
            if win is not None:
                print(f"{win} won")
                run = False
                continue
            if new_state.curr_player.turn == 1:
                # dice_roll = self.logic.roll_dice()
                for event in pygame.event.get():
                    print('get_main')
                    if event.type == pygame.QUIT:
                        print('quit')
                        run = False
                        continue
                # play
                new_state = self.logic.play(new_state, 1)
                print("new_state1:", new_state)
                # self.screen.update(new_state, self.dice_result)
            else:
                # play
                new_state = self.logic.play(new_state, 1)
                print("new_state2:", new_state)
                # self.screen.update(new_state, self.dice_result)

        pygame.quit()


if __name__ == "__main__":
    Main().main()
