class State:
    def __init__(self, board=[], score=0, turn=1):
        self.board = board
        self.score = score
        self.turn = turn
        self.safe = {
            "r": [0, 0, 0, 0, 0],
            "g": [0, 0, 0, 0, 0],
            "b": [0, 0, 0, 0, 0],
            "y": [0, 0, 0, 0, 0],
        }

    def __str__(self):
        return (
            f"                 {self.board[23]} {self.board[24]} {self.board[25]}\n"
            f"                 {self.board[22]} {self.safe['r'][0]}G {self.board[26]}\n"
            f"                 {self.board[21]} {self.safe['r'][1]}G {self.board[27]}\n"
            f"                 {self.board[20]} {self.safe['r'][2]}G {self.board[28]}\n"
            f"                 {self.board[19]} {self.safe['r'][3]}G {self.board[29]}\n"
            f"                 {self.board[18]} {self.safe['r'][4]}G {self.board[30]}\n"
            f"{self.board[12]} {self.board[13]} {self.board[14]} {self.board[15]} {self.board[16]} {self.board[17]}        {self.board[31]} {self.board[32]} {self.board[33]} {self.board[34]} {self.board[35]} {self.board[36]}\n"
            f"{self.board[11]} {self.safe['b'][0]}B {self.safe['b'][1]}B {self.safe['b'][2]}B {self.safe['b'][3]}B {self.safe['b'][4]}B        {self.safe['g'][0]}G {self.safe['g'][1]}G {self.safe['g'][2]}G {self.safe['g'][3]}G {self.safe['g'][3]}G {self.board[37]}\n"
            f"{self.board[10]} {self.board[9]} {self.board[8]} {self.board[7]} {self.board[6]} {self.board[5]}        {self.board[43]} {self.board[42]} {self.board[41]} {self.board[40]} {self.board[39]} {self.board[38]}\n"
            f"                 {self.board[4]} {self.safe['y'][0]}Y {self.board[44]}\n"
            f"                 {self.board[3]} {self.safe['y'][1]}Y {self.board[45]}\n"
            f"                 {self.board[2]} {self.safe['y'][2]}Y {self.board[46]}\n"
            f"                 {self.board[1]} {self.safe['y'][3]}Y {self.board[47]}\n"
            f"                 {self.board[0]} {self.safe['y'][4]}Y {self.board[48]}\n"
            f"                 {self.board[51]} {self.board[50]} {self.board[49]}\n"
        )
        # size = 15  # A typical Ludo self.board is 15x15
        # for i in range(size):
        #     row = self.self.board[i * size:(i + 1) * size]
        #     for node in row:
        #         res += f'{node} '
        #     res += '\n'
        return res