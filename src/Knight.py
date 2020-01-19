from Piece import Piece
from Utility import *

"""
    @desc: The Knight is a piece that can move and attack by moving 1 or 2 steps in one direction and taking another
        2/1 in the perpendicular direction. Its the only piece that can hop over other pieces.
"""
class Knight(Piece):

    """
        @desc: Creates an instance of the Knight object.
        @param team: The team to which the night belongs.
        @param board: The board on which the knight will move on.
        @param x: The horizontal location of the piece.
        @param y: The vertical location of the piece.
    """
    def __init__(self, team, board, x, y):
        super().__init__("n", team, board, x, y)

    """
        @OVERRIDE
        @desc: Checks if a valid move is being made.
        @param move: A move indicating the starting and ending positions of the piece in a string format.
        @return Boolean: Returns True if the move is valid, False otherwise.
    """
    def isValidMove(self, move: str) -> bool:

        intMove = Utility.convertStringMoveToInt(move)
        newX = intMove[2]
        newY = intMove[3]

        xDifference = newX - self.x
        yDifference = newY - self.y

        if [xDifference, yDifference] in self.basicMoves:

            if self.board.isEmpty(newX, newY) == True or self.board.canAttack(newX, newY, self.team):
                return True

        return False