class Node:
    def __init__(self):
        self.is_protected = False
        self.pieces = []

    def protected(self, is_protected):
        self.is_protected = is_protected

    def __str__(self):
        res = ""
        s = len(self.pieces)

        if s == 0:
            if self.is_protected:
                res += f"{s}*"
            else:
                res += f"{s}#"
        else:
            res += f"{s}{self.pieces[0]}"

        return res
