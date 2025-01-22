import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)
WHITE = (255, 255, 255)


class Square:
    def __init__(self, x, y, index, value, color, is_safe=False):
        self.x = x
        self.y = y
        self.size = 21
        self.index = index
        self.value = value
        self.is_safe = is_safe

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
        if color.lower() == "gray":
            self.color = GRAY
        if color.lower() == "red":
            self.color = RED
        elif color.lower() == "green":
            self.color = GREEN
        if color.lower() == "blue":
            self.color = BLUE
        if color.lower() == "yellow":
            self.color = YELLOW

    def draw(self, surface, state):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))
        if type(self.value) == int:
            return
        for i, piece in enumerate(self.value.pieces):
            row = i // 2
            col = i % 2

            cell_size = self.size // 2
            obj_x = self.x + col * cell_size + cell_size // 2
            obj_y = self.y + row * cell_size + cell_size // 2

            piece.draw(surface, (obj_x, obj_y), 5, 7)


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

    def update(self, state, number):
        return
        # self.draw(state, number)

    def get_click(self, pos, state):
        x, y = pos

        if x >= 525 and x <= 630 and y >= 21 and y <= 84:
            return (None, True)

        for sqaure in state.squares:
            if (
                x >= sqaure.x
                and x <= (sqaure.x + sqaure.size)
                and y >= sqaure.y
                and y <= (sqaure.y + sqaure.size)
            ):
                return (sqaure, False)

        return (None, False)

    def draw(self, state, number):
        self.screen.fill(WHITE)
        # dice roll
        dice_color = YELLOW if state.curr_player.team == "y" else RED
        rect1 = pygame.draw.rect(self.screen, dice_color, (21, 21, 63, 63))
        font1 = pygame.font.SysFont("arial", 63)
        text1 = font1.render(f"{number}", True, WHITE)
        title1 = text1.get_rect(center=rect1.center)
        self.screen.blit(text1, title1)

        # add piece
        rect2 = pygame.draw.rect(self.screen, (0, 0, 0), (525, 21, 105, 63))
        font2 = pygame.font.SysFont("arial", 21)
        text2 = font2.render("Add Piece", True, WHITE)
        title2 = text2.get_rect(center=rect2.center)
        self.screen.blit(text2, title2)

        # draw bases
        for i in range(state.base.yellow):
            off = i * 13
            pygame.draw.circle(self.screen, (255, 0, 255), (309 + off, 378), 7)
            pygame.draw.circle(self.screen, (255, 255, 0), (309 + off, 378), 5)

        for i in range(state.base.red):
            off = i * 13
            pygame.draw.circle(self.screen, (255, 0, 255), (309 + off, 273), 7)
            pygame.draw.circle(self.screen, (255, 0, 0), (309 + off, 273), 5)

        # draw player home
        for index, piece in enumerate(state.players[0].get_home_pieces()):
            off = index * 13
            pygame.draw.circle(self.screen, (255, 0, 255), (147 + off, 483), 7)
            pygame.draw.circle(self.screen, (255, 255, 0), (147 + off, 483), 5)
        for index, piece in enumerate(state.players[1].get_home_pieces()):
            off = index * 13
            pygame.draw.circle(self.screen, (255, 0, 255), (483 + off, 147), 7)
            pygame.draw.circle(self.screen, (255, 0, 0), (483 + off, 147), 5)

        # draw squares
        for square in state.squares:
            square.draw(self.screen, state)
        pygame.display.flip()
