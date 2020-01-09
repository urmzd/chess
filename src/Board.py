import Piece

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
    
    """
        @desc: move takes a piece at (x1, y2) and moves it to (x2, y2) as long as the move is valid.
        @param x1: The x location of the piece to be moved.
        @param y1: The y location of the piece to be moved.
        @param x2: The x location the piece is being requested to move to.
        @param y2: The y location the piece is being requested to move to.
    """
    def move(self, x1, y1, x2, y2):
        board[x1][y1].move(x2, y2)

    """
        @desc: Converts lower case alphabets in the ASCII set to a integer.
        @param letter: The ASCII letter to convert.
    """
    def convertY(self, letter):
        return ord(chr(letter)) - 96

    def __str__(self):
        pass
    
    def __repr__(self):
        pass
