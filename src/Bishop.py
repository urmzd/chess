from Piece import Piece
from Utility import *

"""
    @desc: A Bishop is a piece that can only move and attack diagonally.
        It inherits its properties from the Piece class.
"""
class Bishop(Piece):

    """
        @desc: Creates an instance of the Bishop object.
        @param team: The team to which the bishop belongs to.
        @param board: The board on which the piece belongs to.
        @param x: The horizontal location of the piece.
        @param y: The vertical location of the piece.
    """
    def __init__(self, team, board, x, y):
        super().__init__("b", team, board, x, y)
