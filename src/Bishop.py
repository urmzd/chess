from typing import List
from Piece import Piece


class Bishop(Piece):

    """
        Note: Inherits properties from Piece, check Piece.py for more information about attributes.
        @desc: Represents a Bishop in the game of Chess. The Bishop can take any number of steps but only in the diagonal directions.

        @param possibleMoves: The main set involved in the legal movement of the Bishop. Moves can be any set that is a n multiple of this current set.
    """

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, 'B', "\u2657", 30, x, y, board)

        if self.team == "W":
            self.icon = "\u265D"

        self.possibleMoves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    # Read Piece.py documentation for more information regarding this method.
    def validMove(self, x: int, y: int) -> bool:

        # Determine if end position is valid.
        if not self.validPosition(x, y):
            return False

        # Determine the correct set of possibleMoves for the current Bishop.
        possibleMoves = self.getMoveSet(self.possibleMoves)

        xDifference = x - self.x
        yDifference = y - self.y
#        self.possibleMoves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        if xDifference == possibleMoves[0][0] * abs(xDifference):

            if yDifference == possibleMoves[0][1] * abs(yDifference):
                indexNumber = 0
            elif yDifference == possibleMoves[1][1] * abs(yDifference):
                indexNumber = 1
            else:
                return False

        elif xDifference == possibleMoves[2][0] * abs(xDifference):

            if yDifference == possibleMoves[2][1] * abs(yDifference):
                indexNumber = 2
            elif yDifference == possibleMoves[3][1] * abs(yDifference):
                indexNumber = 3
            else:
                return False

        else:
            return False

        xStep = possibleMoves[indexNumber][0]
        yStep = possibleMoves[indexNumber][1]

        tempX = self.x + xStep
        tempY = self.y + yStep

        # Test the path of the Bishop. Ensure all steps are valid.
        while tempX < x or tempY < y:

            if not self.board.isEmpty(tempX, tempY):
                return False

            tempX = tempX + xStep
            tempY = tempY + yStep

        return True

    # Read Piece.py documentation for more information about this method.
    def update(self, x: int, y: int) -> bool:

        # Makes a move and capture if deemed as as a legal movement.
        if self.validMove(x, y):
            self.move(x, y)
            return True
        else:
            print("Illegal move. Try again.")
            return False

    # Reads Piece.py documentation for more information about this method.
    def getAllPossibleMoves(self) -> List[List[int]]:

        possibleMoves = self.getMoveSet(self.possibleMoves)

        validMoves = []

        # Checks what moves are legal and stores them within validMoves.
        for move in possibleMoves:
            tempX = self.x
            tempY = self.y
            while self.board.contains(tempX + move[0], tempY + move[1]):

                # Skip iteration if move already exists within validMoves.
                if [tempX + move[0], tempY + move[1]] in validMoves:
                    tempX = tempX + move[0]
                    tempY = tempY + move[1]
                    continue

                # Store move in validMoves if it is deemed legal.
                if self.validMove(tempX + move[0], tempY + move[1]):
                    validMoves.append([tempX + move[0], tempY + move[1]])

                tempX = tempX + move[0]
                tempY = tempY + move[1]

        return validMoves
