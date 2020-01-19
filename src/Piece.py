from Utility import *
from typing import List

"""
    @desc: The Piece class holds the template for which all other pieces will inherit their
        methods and attributes from.
"""
class Piece():

    """
        @desc: Creates a Piece instance.
        @param name: The name of the piece.
        @param team: The team to which the piece belongs to.
        @param board: The board in which the piece will play on.
        @param x: The horizontal location of the piece.
        @param y: The vertical location of the piece.
    """
    def __init__(self, name: chr, team: chr, board, x: int, y: int):
        self.name = name
        self.team = team
        self.board = board
        self.x = x
        self.y = y
        self.value = Utility.getPieceEvaluation(team, name) # Determine the value of the piece.
        self.icon = Utility.getPieceIcon(team, name) # Determine the icon of the piece.
        self.basicMoves = Utility.getBasicMoves(team, name) # Determine a list of steps the piece can make.
        self.played = False # Indicate if piece has played in the game or not.
        self.possibleMoves = [] # Holds a list of possible moves the piece cna make.

    """
        @desc: Updates the list of possible moves the piece can make.
    """
    def updatePossibleMoves(self):

        self.possibleMoves = [] # Empty possibleMoves after each call.
        
        # Test if each basic move is a possible move.
        for move in self.basicMoves:

            currentPosition = [self.x, self.y]
            moveUpdated = [move[0] + self.x, move[1] + self.y]
            if self.board.contains(moveUpdated[0], moveUpdated[1]) == False:
                continue
            actualMove = currentPosition + moveUpdated
            stringMove = Utility.convertIntMoveToString(actualMove)

            if self.isValidMove(stringMove) and move not in self.possibleMoves:
                self.possibleMoves.append(stringMove)
            

    """
        @desc: Checks if a move is valid or not. Default method meant for Bishop, Rook and Queen.
        @param move: A string representation of the move to be made.
        @return Boolean: Returns True if the move is valid, False otherwise.
    """
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

    """
        @desc: Checks if a moves path is valid.
        @param: The move to check.
        @return Boolean: Checks if all squares up until the destination point is empty. Returns true if they are, False otherwise.
    """
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

        if self.board.isEmpty(newMove[0], newMove[1]) == False and self.board.isFriendly(newMove[0], newMove[1], self.team) == True:
            return False
        else:
            while tempMove != newMove:

                if self.board.contains(tempMove[0], tempMove[1]) == False:
                    return False
                elif self.board.isEmpty(tempMove[0], tempMove[1]) == False:
                    return False
                else:
                    tempMove[0] += xStep
                    tempMove[1] += yStep

        return True

    """
        @desc: Updates the move counter on the board depending on the situation.
        @param x: The horizontal location of the piece.
        @param y: The vertical location of the piece.
    """
    def updateCounter(self, x: int, y: int):

        if self.board.canAttack(x, y, self.team):
            self.board.resetCounter() # Resets counter a piece is going to be removed.
        else:
            self.board.incrementCounter() # Increment counter otherwise.

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

    """
        @desc: Represents the piece in unicode.
        @return String: The unicode to print out.
    """
    def __repr__(self):
        return self.icon