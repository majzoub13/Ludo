import pygame


class Piece:
    def __init__(self, team, id):
        self.inBase = False
        self.counter = 0
        self.team = team
        self.safe = None
        self.pos = None
        self.id = id

        self.COLOR = {
            "r": (255, 0, 0),
            "g": (0, 255, 0),
            "b": (0, 0, 255),
            "y": (255, 255, 0),
        }

    def __str__(self):
        return self.team

    def __eq__(self, other):
        # need to add |None check because None cant have pos
        if other is None:
            return False
        return self.pos == other.pos

    def draw(self, screen, position, radius):
        color = self.COLOR.get(self.team)
        pygame.draw.circle(screen, color, position, radius)
