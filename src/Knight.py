from Piece import Piece
from Utility import *

class Knight(Piece):

    def __init__(self, team, board, x, y):
        super().__init__("n", team, board, x, y)

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