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
        self.score = 0

        self.players = players
        self.curr_player = players[0]

        self.squares = [
            # Board Squares
            Square(273, 567, 0, self.board[0], "black"),
            Square(273, 525, 1, self.board[1], "black"),
            Square(273, 483, 2, self.board[2], "black"),
            Square(273, 441, 3, self.board[3], "black"),
            Square(273, 399, 4, self.board[4], "black"),
            Square(231, 357, 5, self.board[5], "black"),
            Square(189, 357, 6, self.board[6], "black"),
            Square(147, 357, 7, self.board[7], "black"),
            Square(105, 357, 8, self.board[8], "black"),
            Square(63, 357, 9, self.board[9], "black"),
            Square(21, 357, 10, self.board[10], "black"),
            Square(21, 315, 11, self.board[11], "black"),
            Square(21, 273, 12, self.board[12], "black"),
            Square(63, 273, 13, self.board[13], "black"),
            Square(105, 273, 14, self.board[14], "black"),
            Square(147, 273, 15, self.board[15], "black"),
            Square(189, 273, 16, self.board[16], "black"),
            Square(231, 273, 17, self.board[17], "black"),
            Square(273, 231, 18, self.board[18], "black"),
            Square(273, 189, 19, self.board[19], "black"),
            Square(273, 147, 20, self.board[20], "black"),
            Square(273, 105, 21, self.board[21], "black"),
            Square(273, 63, 22, self.board[22], "black"),
            Square(273, 21, 23, self.board[23], "black"),
            Square(315, 21, 24, self.board[24], "black"),
            Square(357, 21, 25, self.board[25], "black"),
            Square(357, 63, 26, self.board[26], "black"),
            Square(357, 105, 27, self.board[27], "black"),
            Square(357, 147, 28, self.board[28], "black"),
            Square(357, 189, 29, self.board[29], "black"),
            Square(357, 231, 30, self.board[30], "black"),
            Square(399, 273, 31, self.board[31], "black"),
            Square(441, 273, 32, self.board[32], "black"),
            Square(483, 273, 33, self.board[33], "black"),
            Square(525, 273, 34, self.board[34], "black"),
            Square(567, 273, 35, self.board[35], "black"),
            Square(609, 273, 36, self.board[36], "black"),
            Square(609, 315, 37, self.board[37], "black"),
            Square(609, 357, 38, self.board[38], "black"),
            Square(567, 357, 39, self.board[39], "black"),
            Square(525, 357, 40, self.board[40], "black"),
            Square(483, 357, 41, self.board[41], "black"),
            Square(441, 357, 42, self.board[42], "black"),
            Square(399, 357, 43, self.board[43], "black"),
            Square(357, 399, 44, self.board[44], "black"),
            Square(357, 441, 45, self.board[45], "black"),
            Square(357, 483, 46, self.board[46], "black"),
            Square(357, 525, 47, self.board[47], "black"),
            Square(357, 567, 48, self.board[48], "black"),
            Square(357, 609, 49, self.board[49], "black"),
            Square(315, 609, 50, self.board[50], "black"),
            Square(273, 609, 51, self.board[51], "black"),
            # Safe Squares
            Square(315, 567, 0, self.safe[1][0], "yellow", True),
            Square(315, 525, 1, self.safe[1][1], "yellow", True),
            Square(315, 483, 2, self.safe[1][2], "yellow", True),
            Square(315, 441, 3, self.safe[1][3], "yellow", True),
            Square(315, 399, 4, self.safe[1][4], "yellow", True),
            Square(315, 63, 0, self.safe[-1][0], "red", True),
            Square(315, 105, 1, self.safe[-1][1], "red", True),
            Square(315, 147, 2, self.safe[-1][2], "red", True),
            Square(315, 189, 3, self.safe[-1][3], "red", True),
            Square(315, 231, 4, self.safe[-1][4], "red", True),
            Square(567, 315, 0, self.safe["g"][0], "green", True),
            Square(525, 315, 1, self.safe["g"][1], "green", True),
            Square(483, 315, 2, self.safe["g"][2], "green", True),
            Square(441, 315, 3, self.safe["g"][3], "green", True),
            Square(399, 315, 4, self.safe["g"][4], "green", True),
            Square(63, 315, 0, self.safe["b"][0], "blue", True),
            Square(105, 315, 1, self.safe["b"][1], "blue", True),
            Square(147, 315, 2, self.safe["b"][2], "blue", True),
            Square(189, 315, 3, self.safe["b"][3], "blue", True),
            Square(231, 315, 4, self.safe["b"][4], "blue", True),
        ]

    def __str__(self):
        return (
            f"\n"
            f"The pieces for player1 pos is {self.players[0].pieces[0].pos} , {self.players[0].pieces[1].pos} ,{self.players[0].pieces[2].pos}, {self.players[0].pieces[3].pos}\n"
            f"The pieces for player2 pos is {self.players[1].pieces[0].pos} , {self.players[1].pieces[1].pos} ,{self.players[1].pieces[2].pos}, {self.players[1].pieces[3].pos}\n"
            f"The pieces for player1 safe is {self.players[0].pieces[0].safe} , {self.players[0].pieces[1].safe} ,{self.players[0].pieces[2].safe}, {self.players[0].pieces[3].safe}\n"
            f"The pieces for player2 safe is {self.players[1].pieces[0].safe} , {self.players[1].pieces[1].safe} ,{self.players[1].pieces[2].safe}, {self.players[1].pieces[3].safe}\n"
            f"\n"
            f"                       {self.board[23]}# {self.board[24]}# {self.board[25]}#\n"
            f"                       {self.board[22]}# {self.safe[-1][0]}R {self.board[26]}*\n"
            f"                       {self.board[21]}* {self.safe[-1][1]}R {self.board[27]}#\n"
            f"                       {self.board[20]}# {self.safe[-1][2]}R {self.board[28]}#\n"
            f"                       {self.board[19]}# {self.safe[-1][3]}R {self.board[29]}#\n"
            f"                       {self.board[18]}# {self.safe[-1][4]}R {self.board[30]}#\n"
            f"{self.board[12]}# {self.board[13]}* {self.board[14]}# {self.board[15]}# {self.board[16]}# {self.board[17]}#           {self.board[31]}# {self.board[32]}# {self.board[33]}# {self.board[34]}* {self.board[35]}# {self.board[36]}#\n"
            f"{self.board[11]}# {self.safe['b'][0]}B {self.safe['b'][1]}B {self.safe['b'][2]}B {self.safe['b'][3]}B {self.safe['b'][4]}B           {self.safe['g'][4]}G {self.safe['g'][3]}G {self.safe['g'][2]}G {self.safe['g'][1]}G {self.safe['g'][0]}G {self.board[37]}#\n"
            f"{self.board[10]}# {self.board[9]}# {self.board[8]}* {self.board[7]}# {self.board[6]}# {self.board[5]}#           {self.board[43]}# {self.board[42]}# {self.board[41]}# {self.board[40]}# {self.board[39]}* {self.board[38]}#\n"
            f"                       {self.board[4]}# {self.safe[1][4]}Y {self.board[44]}#\n"
            f"                       {self.board[3]}# {self.safe[1][3]}Y {self.board[45]}#\n"
            f"                       {self.board[2]}# {self.safe[1][2]}Y {self.board[46]}#\n"
            f"                       {self.board[1]}# {self.safe[1][1]}Y {self.board[47]}*\n"
            f"                       {self.board[0]}* {self.safe[1][0]}Y {self.board[48]}#\n"
            f"                       {self.board[51]}# {self.board[50]}# {self.board[49]}#\n"
        )
