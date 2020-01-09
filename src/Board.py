import Pieces.py

class Board:

    def __init__(self, board):
        self.board = []
        self.counter = 0
        self.lastMove = ""

    def move(self, x1, y1, x2, y2):
        board[x1][y1].move(x2, y2)

    def convertY(self, y):
        return ord(chr(y)) - 96

    def __str__(self):
        pass
    
    def __repr__(self):
        pass
