from typing import List
from Piece import Piece

class Bishop(Piece):

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, 'B', "\u2657", 3, x, y, board)
    
    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x,y):
            return False
        
        possibleMoves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        self.inverseMoveSet(possibleMoves, self.team)

        xDifference = x - self.x
        yDifference = y - self.y
        
        if xDifference == possibleMoves[0][0] * xDifference:

            if yDifference == possibleMoves[0][1] * yDifference:
                indexNumber = 0
            elif yDifference == possibleMoves[1][1] * yDifference:
                indexNumber = 1
            else:
                return False
        
        elif xDifference == possibleMoves[2][0] * xDifference:

            if yDifference == possibleMoves[2][1] * yDifference:
                indexNumber = 2
            elif yDifference == possibleMoves[3][1] * yDifference:
                indexNumber = 3
            else:
                return False

        else:
            return False

        xStep = possibleMoves[indexNumber][0]
        yStep = possibleMoves[indexNumber][1]

        tempX = self.x + xStep
        tempY = self.y + yStep

        while tempX < x and tempY < y:

            if not self.board.isEmpty(tempX, tempY):
                return False

        return True
    
    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            self.move(x, y)

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass