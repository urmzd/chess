from Piece import Piece
from Utility import *

"""
    @desc: The Rook can move only in straight lines.
"""
class Rook(Piece):

    """
        @desc: Creates an instance of the Queen object.
        @param team: The team to which the piece belongs to.
        @param board: The board on which the piece will move on.
        @param x: The horizontal
    """
    def __init__(self, team, board, x, y):
        super().__init__("r", team, board, x, y)
