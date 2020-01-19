from Piece import Piece
from Utility import *

"""
    @desc: The Queen can move any number of steps in any direction as long it is a valid path.
"""
class Queen(Piece):

    """
        @desc: Creates an instance of the Queen object.
        @param team: The team to which the piece belongs to.
        @param board: The board on which the piece will move on.
        @param x: The horizontal 
    """
    def __init__(self, team, board, x, y):
        super().__init__("q", team, board, x, y)