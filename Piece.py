class Piece:
    def __init__(self, team):
        self.counter = 0
        self.team = team
        self.pos = None
        return

    def __str__(self):
        return self.team

    def __eq__(self, other):
        return self.pos == other.pos
