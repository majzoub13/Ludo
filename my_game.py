import pygame
import sys

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Square:
    def __init__(self, x, y, value, color):
        self.x = x
        self.y = y
        self.size = 21
        self.value = value

        # self.COLOR = {
        #     "red": (255, 0, 0),
        #     "green": (0, 255, 0),
        #     "blue": (0, 0, 255),
        #     "yellow": (255, 255, 0),
        #     "black": (0, 0, 0),
        #     "white": (0, 0, 0),
        # }

        if color.lower() == "black":
            self.color = BLACK
        if color.lower() == "red":
            self.color = RED
        elif color.lower() == "green":
            self.color = GREEN
        if color.lower() == "blue":
            self.color = BLUE
        if color.lower() == "yellow":
            self.color = YELLOW

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))
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


class LudoScreen:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LudoScreen, cls).__new__(cls)
            cls._instance.__init_instance()
        return cls._instance

    def __init_instance(self):
        print("LudoScreen")
        self.width, self.height = 651, 651
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ludo")

    def draw(self, state):
        print("white")
        self.screen.fill(WHITE)
        for square in state.squares:
            square.draw(self.screen)
        pygame.display.flip()
