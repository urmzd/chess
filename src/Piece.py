from Utility import *
from typing import List

class Piece():

    def __init__(self, name: chr, team: chr, board, x: int, y: int):
        self.name = name
        self.team = team
        self.board = board
        self.x = x
        self.y = y
        self.value = Utility.getPieceEvaluation(team, name)
        self.icon = Utility.getPieceIcon(team, name)
        self.basicMoves = Utility.getBasicMoves(team, name)
        self.played = False
        self.possibleMoves = []

    def updatePossibleMoves(self):

        self.possibleMoves = [] # Empty possibleMoves after each call.
        
        for move in self.basicMoves:

            currentPosition = [self.x, self.y]
            moveUpdated = [move[0] + self.x, move[1] + self.y]
            if self.board.contains(moveUpdated[0], moveUpdated[1]) == False:
                continue
            actualMove = currentPosition + moveUpdated
            stringMove = Utility.convertIntMoveToString(actualMove)

            if self.isValidMove(stringMove) and move not in self.possibleMoves:
                self.possibleMoves.append(stringMove)
            

    def isValidMove(self, move: str) -> bool:
        pass

    def isValidPath(self, move: str) -> bool:

        intMove = Utility.convertStringMoveToInt(move)
        newX = intMove[2]
        newY = intMove[3]
        newMove = [newX, newY]

        xDifference = newX - self.x
        yDifference = newY - self.y

        xStep = int(xDifference / abs(xDifference)) if xDifference != 0 else 0
        yStep = int(yDifference / abs(yDifference)) if yDifference != 0 else 0

        tempX = self.x + xStep
        tempY = self.y + yStep

        tempMove = [tempX, tempY]

        if self.board.contains(newX, newY) == False:
            return False
        
        if self.board.isEmpty(newMove[0], newMove[1]) == False:
            if self.board.isFriendly(newMove[0], newMove[1], self.team) == True:
                return False
 
        if self.board.isEmpty(tempMove[0], tempMove[1]) == False:
            return False
        else:
            while tempMove != newMove:

                if self.board.isEmpty(tempMove[0], tempMove[1]) == False:
                    return False
                else:
                    tempMove[0] += xStep
                    tempMove[1] += yStep

        return True

    def updateCounter(self, x: int, y: int):

        if self.board.canAttack(x, y, self.team):
            self.board.resetCounter()
        else:
            self.board.incrementCounter()

    def move(self, move: str) -> bool:

        if move in self.possibleMoves:
            intMove = Utility.convertStringMoveToInt(move)
            currentX = intMove[0]
            currentY = intMove[1]
            newX = intMove[2]
            newY = intMove[3]
            self.board.removePiece(currentX, currentY)
            self.updateCounter(newX, newY)
            self.board.addPiece(self, newX, newY)
            self.x = newX
            self.y = newY

            if self.played == False:
                self.played = True
            
            self.board.lastMove = self.name + move
        else:
            print(move + " " + "is an illegal move. Try again")
            return False

    def __repr__(self):
        return self.icon