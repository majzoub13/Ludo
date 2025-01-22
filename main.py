from Logic import Logic
from State import State
from Player import Player
from LudoScreen import LudoScreen
from copy import deepcopy
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
        self.screen.draw(self.init_state, "")

    def main(self):
        new_state = deepcopy(self.init_state)
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
                    print("get_main")
                    if event.type == pygame.QUIT:
                        print("quit")
                        run = False
                        continue
                # play
                new_state = self.logic.play(new_state, 1)
                if new_state is False:
                    run = False
                    continue
                print("new_state1:", new_state)
            else:
                # play
                new_state = self.logic.play(new_state, 1)
                print("new_state2:", new_state)

        pygame.quit()

    # main no GUI

    # def main(self):
    #     new_state = self.logic.move(self.init_state, 1)

    #     while True:
    #         win = self.logic.check_win(new_state.base)
    #         if win is not None:
    #             print(self.check_win(new_state.base) + " won")
    #             break

    #         new_state = self.logic.move(new_state, 1)


if __name__ == "__main__":
    Main().main()
