from Base import Base
from LudoNode import Node
from my_game import Square


class State:
    def __init__(self, players):
        self.board = [Node() for _ in range(52)]
        self.safe = {
            -1: [Node() for _ in range(5)],
            "g": [Node() for _ in range(5)],
            "b": [Node() for _ in range(5)],
            1: [Node() for _ in range(5)],
        }
        self.base = Base()

        self.players = players
        self.curr_player = players[0]
        self.score = 0
        self.height = 730
        self.padding = 40
        self.squares = [
            Square(300, 650, self.board[0]),
            Square(300, 600, self.board[1]),
            Square(300, 550, self.board[2]),
            Square(300, 500, self.board[3]),
            Square(300, 450, self.board[4]),
            Square(250, (self.height / 2) + self.padding, self.board[5]),
            Square(150, (self.height / 2) + self.padding, self.board[7]),
            Square(100, (self.height / 2) + self.padding, self.board[8]),
            Square(50, (self.height / 2) + self.padding, self.board[9]),
            Square(0, (self.height / 2) + self.padding, self.board[10]),
            Square(0, (self.height / 2), self.board[11]),
            Square(0, (self.height / 2) - self.padding, self.board[12]),
            Square(50, (self.height / 2) - self.padding, self.board[13]),
            Square(100, (self.height / 2) - self.padding, self.board[14]),
            Square(150, (self.height / 2) - self.padding, self.board[15]),
            Square(200, (self.height / 2) - self.padding, self.board[16]),
            Square(250, (self.height / 2) - self.padding, self.board[17]),
            Square(300, 280, self.board[18]),
            Square(300, 230, self.board[19]),
            Square(300, 180, self.board[20]),
            Square(300, 130, self.board[21]),
            Square(300, 80, self.board[22]),
            Square(300, 20, self.board[23]),
            Square(350, 20, self.board[24]),
            Square(400, 20, self.board[25]),
            Square(400, 80, self.board[26]),
            Square(400, 130, self.board[27]),
            Square(400, 180, self.board[28]),
            Square(400, 230, self.board[29]),
            Square(400, 280, self.board[30]),
            Square(450, (self.height / 2) - self.padding, self.board[31]),
            Square(500, (self.height / 2) - self.padding, self.board[32]),
            Square(550, (self.height / 2) - self.padding, self.board[33]),
            Square(600, (self.height / 2) - self.padding, self.board[34]),
            Square(650, (self.height / 2) - self.padding, self.board[35]),
            Square(700, (self.height / 2) - self.padding, self.board[36]),
            Square(700, (self.height / 2), self.board[37]),
            Square(700, (self.height / 2) + self.padding, self.board[38]),
            Square(650, (self.height / 2) + self.padding, self.board[39]),
            Square(600, (self.height / 2) + self.padding, self.board[40]),
            Square(550, (self.height / 2) + self.padding, self.board[41]),
            Square(500, (self.height / 2) + self.padding, self.board[42]),
            Square(450, (self.height / 2) + self.padding, self.board[43]),
            Square(400, 450, self.board[44]),
            Square(400, 500, self.board[45]),
            Square(400, 550, self.board[46]),
            Square(400, 600, self.board[47]),
            Square(400, 650, self.board[48]),
            Square(400, 700, self.board[49]),
            Square(350, 700, self.board[50]),
            Square(200, (self.height / 2) + self.padding, 0),
            Square(300, (self.height / 2) + self.padding, 0),
            Square(350, (self.height / 2) + self.padding, 0),
            Square(400, (self.height / 2) + self.padding, 0),
            Square(300, (self.height / 2) - self.padding, 0),
            Square(350, (self.height / 2) - self.padding, 0),
            Square(400, (self.height / 2) - self.padding, 0),
            Square(50, (self.height / 2), 0),
            Square(100, (self.height / 2), 0),
            Square(150, (self.height / 2), 0),
            Square(200, (self.height / 2), 0),
            Square(250, (self.height / 2), 0),
            Square(300, (self.height / 2), 0),
            Square(350, (self.height / 2), 0),
            Square(400, (self.height / 2), 0),
            Square(450, (self.height / 2), 0),
            Square(500, (self.height / 2), 0),
            Square(550, (self.height / 2), 0),
            Square(600, (self.height / 2), 0),
            Square(650, (self.height / 2), 0),
            Square(350, 80, 0),
            Square(350, 130, 0),
            Square(350, 180, 0),
            Square(350, 230, 0),
            Square(350, 280, 0),
            Square(350, 450, 0),
            Square(350, 500, 0),
            Square(350, 550, 0),
            Square(350, 600, 0),
            Square(350, 650, 0),
        ]

    def __str__(self):
        return (
            f"\n"
            f"The pieces for player1 pos is {self.players[0].pieces[0].pos} , {self.players[0].pieces[1].pos} ,{self.players[0].pieces[2].pos}, {self.players[0].pieces[3].pos}\n"
            f"The pieces for player2 pos is {self.players[1].pieces[0].pos} , {self.players[1].pieces[1].pos} ,{self.players[1].pieces[2].pos}, {self.players[1].pieces[3].pos}\n"
            f"The pieces for player1 safe is {self.players[0].pieces[0].safe} , {self.players[0].pieces[1].safe} ,{self.players[0].pieces[2].safe}, {self.players[0].pieces[3].safe}\n"
            f"The pieces for player2 safe is {self.players[1].pieces[0].safe} , {self.players[1].pieces[1].safe} ,{self.players[1].pieces[2].safe}, {self.players[1].pieces[3].safe}\n"
            f"\n"
            f"                 {self.board[23]} {self.board[24]} {self.board[25]}\n"
            f"                 {self.board[22]} {self.safe[-1][0]}R {self.board[26]}\n"
            f"                 {self.board[21]} {self.safe[-1][1]}R {self.board[27]}\n"
            f"                 {self.board[20]} {self.safe[-1][2]}R {self.board[28]}\n"
            f"                 {self.board[19]} {self.safe[-1][3]}R {self.board[29]}\n"
            f"                 {self.board[18]} {self.safe[-1][4]}R {self.board[30]}\n"
            f"{self.board[12]} {self.board[13]} {self.board[14]} {self.board[15]} {self.board[16]} {self.board[17]}        {self.board[31]} {self.board[32]} {self.board[33]} {self.board[34]} {self.board[35]} {self.board[36]}\n"
            f"{self.board[11]} {self.safe['b'][0]}B {self.safe['b'][1]}B {self.safe['b'][2]}B {self.safe['b'][3]}B {self.safe['b'][4]}B        {self.safe['g'][4]}G {self.safe['g'][3]}G {self.safe['g'][2]}G {self.safe['g'][1]}G {self.safe['g'][0]}G {self.board[37]}\n"
            f"{self.board[10]} {self.board[9]} {self.board[8]} {self.board[7]} {self.board[6]} {self.board[5]}        {self.board[43]} {self.board[42]} {self.board[41]} {self.board[40]} {self.board[39]} {self.board[38]}\n"
            f"                 {self.board[4]} {self.safe[1][4]}Y {self.board[44]}\n"
            f"                 {self.board[3]} {self.safe[1][3]}Y {self.board[45]}\n"
            f"                 {self.board[2]} {self.safe[1][2]}Y {self.board[46]}\n"
            f"                 {self.board[1]} {self.safe[1][1]}Y {self.board[47]}\n"
            f"                 {self.board[0]} {self.safe[1][0]}Y {self.board[48]}\n"
            f"                 {self.board[51]} {self.board[50]} {self.board[49]}\n"
        )
