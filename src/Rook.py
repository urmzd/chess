from typing import List
from Piece import Piece


class Rook(Piece):

    """
        Note: Inherits properties from Piece, check Piece.py for more information about attributes.
        @desc: Represents a Rook in the game of Chess. The Rook can make any number of moves but only in the horizontal/vertical plane.
            It is also involved in castling. Refer to the King class for more information about how this works.

        @param possibleMoves: A set of the possible moves that can be made by the Rook. All legal moves are n multiples of the set.
        @param played: Indicates whether the piece has been played or not in the game.
    """

    def __init__(self, team: str, x: int, y: int, board: "Board"):
        super().__init__(team, "R", "\u2656", 50, x, y, board)

        if self.team == "W":
            self.icon = "\u265C"

        self.possibleMoves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.played = False

    # Refer to Pieces.py documentation for more information.
    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x, y):
            return False

        possibleMoves = self.getMoveSet(self.possibleMoves)

        xDifference = x - self.x
        yDifference = y - self.y

        if xDifference == possibleMoves[0][0] * xDifference:

            if yDifference == possibleMoves[0][1] * yDifference:
                indexNumber = 0
            elif yDifference == possibleMoves[1][1] * yDifference:
                indexNumber = 1
            else:
                return False

        elif yDifference == possibleMoves[2][1] * yDifference:

            if xDifference == possibleMoves[2][0] * xDifference:
                indexNumber = 2
            elif xDifference == possibleMoves[3][0] * xDifference:
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

    # Refer to Pieces.py documentation for more information.
    def update(self, x: int, y: int) -> bool:

        if self.validMove(x, y):

            if self.played == False:
                self.played = True

            self.move(x, y)
            return True
        else:
            print("Illegal move. Try again.")
            return False

    # Refer to Pieces.py documentation for more information.
    def getAllPossibleMoves(self) -> List[List[int]]:

        possibleMoves = self.getMoveSet(self.possibleMoves)
        validMoves = []

        tempX = self.x
        tempY = self.y

        for move in possibleMoves:
            tempX = self.x
            tempY = self.y
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
