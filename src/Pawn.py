from Utility import *
from Piece import Piece
from typing import List

"""
    @desc: The Pawn is a piece that can only attack diagonally and move vertically. It can make two steps on the first move,
        otherwise it must only make a one step move. The Pawn can also make an en passent which allows it to take the piece behind it
        given that the opponents pawn moved two steps forward in order to avoid capture.
        
"""
class Pawn(Piece):

    """
        @desc: Creates an instance of the Pawn object.
        @param team: The team to which the pawn belongs to.
        @param board: The board to which the piece will move on.
        @param x: The horizontal location of the piece.
        @param y: The vertical location of the piece.
    """
    def __init__(self, team, board, x, y):
        super().__init__("p", team, board, x, y)
        self.passentAttempt = False
        self.isAI = False
    
    """
        @OVERRIDE
        @desc: Determines if a move can be made.
        @param move: A string indicating the starting and ending positions of the piece.
        @return Boolean: Returns True if a move can be made, False otherwise.
    """
    def isValidMove(self, move: str) -> bool:

        intMove = Utility.convertStringMoveToInt(move)
        newX = intMove[2]
        newY = intMove[3]

        xDifference = newX - self.x
        yDifference = newY - self.y

        if [xDifference, yDifference] in self.basicMoves:

            if abs(xDifference) == 1 and abs(yDifference) == 1:

                if self.board.canAttack(newX, newY, self.team):
                    return True
                else:
                    lastMove = self.board.lastMove

                    if lastMove != "" and lastMove[0] == "p":
                        intMoves = Utility.convertStringMoveToInt(lastMove[1:5])
                        currentX = intMoves[0]
                        currentY = intMoves[1]
                        newX = intMoves[2]
                        newY = intMoves[3]

                        if abs(newY - self.y) != 1:
                            return False

                        if newX - currentX == 0 and abs(newY - currentY) == 2:
                            if currentX + 1 == self.x or currentX - 1 == self.x:
                                self.passentAttempt = True
                                return True
                    else:
                        return False
                     
            elif abs(xDifference) == 0 and abs(yDifference) == 2:

                if self.played == False and self.board.isEmpty(newX, newY):
                    if self.isValidPath(move):
                        return True
                    else:
                        return False
                else:
                    return False

            else:
                if self.board.isEmpty(newX, newY):
                    return True
        else:
            return False

        return False

    """
        @OVERRIDE
        @desc: Moves the piece to a new position and promotes the piece if requirements are met (ends of board is reached).
        @move: A string indicating the starting and eneding positions of the piece.
    """
    def move(self, move: str) -> bool:

        if move in self.possibleMoves:
            intMove = Utility.convertStringMoveToInt(move)
            currentX = intMove[0]
            currentY = intMove[1]
            newX = intMove[2]
            newY = intMove[3]
            self.board.removePiece(currentX, currentY)
            self.board.resetCounter()
            if self.passentAttempt == True:
                if self.team == "W":
                    self.board.removePiece(newX, newY - 1)
                else:
                    self.board.removePiece(newX, newY + 1)
                self.passentAttempt == False
            self.board.addPiece(self, newX, newY)

            self.x = newX
            self.y = newY

            if self.played == False:
                self.played = True

            if newY == 0 or newY == 7:

                if self.isAI == False:
                    name = input("What piece would like to upgrade to. Enter the first lower case letter of the piece, n for knight:")
                    choices = ["q", "n", "b", "r"]
                    if name not in choices :
                        while name not in choices:
                            name = input("What piece would like to upgrade to. Enter the first lower case letter of the piece, n for knight:")

                            if name in choices:
                                break
                else:
                    name = "q"

                self.board.promotePawn(self.x, self.y, self.team, name)
            
            self.board.lastMove = self.name + move
        else:
            print(move + " " + "is an illegal move. Try again")
            return False
    