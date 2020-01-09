import Pieces.py

"""
    @desc: The Board class holds all the pieces in the game and contains methods to 
    update the position of the pieces and attributes to hold information for rules such
    as the 50-move rule and threefold-repetition rule.
"""
class Board:

    """
        @desc: A constructor which create a board for the chess pieces to move on.
    """
    def __init__(self):
        self.board = [] # A 8 x 8 board.
        self.counter = 0 # Number of moves since the last capture or pawn move.
        self.lastMove = "" # A string to hold the last move made in string format.
    
    def move(self, x1, y1, x2, y2):
        board[x1][y1].move(x2, y2)

    def convertY(self, y):
        return ord(chr(y)) - 96

    def __str__(self):
        pass
    
    def __repr__(self):
        pass
