import Pieces.py

class Board:

    def __init__(self, board):
        self.board = [[Rook()]]
        self.counter = 0 # Counts the number of moves since last pawn move or capture
        self.lastMove = ""
    
    # Updates board information.
    def update(self):
        pass

    # Converts char to int.
    def convertY(self, y):
        return ord(chr(y)) - 96

    # Prints board using string representation.
    def __str__(self):
        pass
    
    # Representation of board.
    def __repr__(self):
        pass
