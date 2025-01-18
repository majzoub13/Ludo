from Base import Base
from LudoNode import Node


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

    def __str__(self):
        return (
            f"The pices for player1 is {self.players[0].pieces[0].pos} , {self.players[0].pieces[1].pos} ,{self.players[0].pieces[2].pos}, {self.players[0].pieces[3].pos}\n"
            f"The pices for player2 is {self.players[1].pieces[0].pos} , {self.players[1].pieces[1].pos} ,{self.players[1].pieces[2].pos}, {self.players[1].pieces[3].pos}\n"
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
