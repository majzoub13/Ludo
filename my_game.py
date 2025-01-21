import pygame
import sys


WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Square:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.size = 30
        self.value = value

    # def draw(self, surface):
    #     pygame.draw.rect(surface, RED, (self.x, self.y, self.size, self.size))

    #     font = pygame.font.Font(None, 36)
    #     text_surface = font.render(str(self.value), True, WHITE)

    #     text_rect = text_surface.get_rect(
    #         center=(self.x + self.size // 2, self.y + self.size // 2)
    #     )

    #     surface.blit(text_surface, text_rect)
    def draw(self, surface):
            pygame.draw.rect(surface, RED, (self.x, self.y, self.size, self.size))
            if type(self.value) == int:
                return
            for i, piece in enumerate(self.value.pieces):
                print(piece)
                row = i // 2
                col = i % 2

                cell_size = self.size // 2
                obj_x = self.x + col * cell_size + cell_size // 2
                obj_y = self.y + row * cell_size + cell_size // 2

                piece.draw(surface, (obj_x, obj_y), 4)




def update_screen(state):
    pass


def start_screen(state):
    pass


# Initialize Pyga


# Define colors


padding = 40



WHITE = (255, 255, 255)

class LudoScreen:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LudoScreen, cls).__new__(cls)
            cls._instance.__init_instance()
        return cls._instance

    def __init_instance(self):
        print("LudoScreen")
        self.width, self.height = 730, 730
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ludo")

    def draw(self, state):
        print("white")
        self.screen.fill(WHITE)
        for square in state.squares:
            square.draw(self.screen)
        pygame.display.flip()