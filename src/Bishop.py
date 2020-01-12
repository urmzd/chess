from typing import List
from Piece import Piece

class Bishop(Piece):


    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, 'B', "\u2657", 3, x, y, board)
        self.possibleValues = possibleMoves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        if self.team == "W":
            self.icon = "\u265D"
    
    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x,y):
            return False
        
        possibleMoves = self.getMoveSet()

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
            
            tempX = tempX + xStep
            tempY = tempY + yStep

        return True
    
    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            self.move(x, y)
        else:
            print("X")

    def getAllPossibleMoves(self) -> List[List[int]]:

        possibleMoves = self.getMoveSet(self.possibleMoves, self.team)
        validMoves = []

        tempX = self.x
        tempY = self.y

        for move in possibleMoves:
            while self.board.contains(tempX + move[0], tempY + move[1]):
                
                if [tempX + move[0], tempY + move[1]] in validMoves:
                    tempX = tempX + move[0]
                    tempY = tempY + move[1]
                    continue

                if self.validMove(tempX + move[0], tempY + move[1]):
                    validMoves.append([tempX + move[0], tempY + move[1]])

                tempX = tempX + move[0]
                tempY = tempY + move[1]
        
        return validMoves
