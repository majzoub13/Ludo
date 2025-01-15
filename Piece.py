class Piece:
    def __init__(self, team):
        self.counter = 0
        self.team = team
        self.pos = None
        return

    def __str__(self):
        return self.team

    def __eq__(self, other):
        # need to add |None check because None cant have pos
        if other == None:
            return False
        return self.pos == other.pos
