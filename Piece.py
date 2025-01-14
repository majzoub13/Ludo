class Piece:
    def __init__(self, team, position):
        self.counter = 0
        self.team = team
        self.position = position
        return

    def __str__(self):
        return self.team
