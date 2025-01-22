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
        self.dice_result = None

    def main(self):
        new_state = self.logic.move(self.init_state, 1)
        selected_piece_id = None
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #pos = pygame.mouse.get_pos()  # Get mouse position

                    self.dice_result = self.logic.roll_dice()
                    print(f"Dice rolled: {self.dice_result}")
                    if selected_piece_id is None:
                        # Check if a piece was clicked
                        pass
                    else:
                        # Move the selected piece using the dice result
                        new_state = self.logic.move(new_state, 1, self.dice_result, selected_piece_id)
                        selected_piece_id = None
                        self.dice_result = None

                    new_state = self.logic.move(new_state, 1, self.dice_result, selected_piece_id)
            win = self.logic.check_win(new_state.base)
            if win is not None:
                print(f"{win} won")
                run = False
            self.screen.update(new_state, self.dice_result)

        pygame.quit()


if __name__ == "__main__":
    Main().main()
