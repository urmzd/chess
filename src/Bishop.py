from Piece import Piece
from Utility import *

class Bishop(Piece):

    def __init__(self, team, board, x, y):
        super().__init__("b", team, board, x, y)

    def isValidMove(self, move: str) -> bool:
        
        intMove = Utility.convertStringMoveToInt(move)
        newX = intMove[2]
        newY = intMove[3]

        xDifference = newX - self.x
        yDifference = newY - self.y

        if [xDifference, yDifference] in self.basicMoves:

            if self.isValidPath(move):
                return True

        return False