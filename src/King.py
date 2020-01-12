from Piece import Piece
from Rook import Rook


class King(Piece):

    """
        Note: Inherits properties from Piece, check Piece.py for more information about attributes.
        @desc: Represents the King in the game of Chess. This piece is the most important piece in the game as losing this piece
            means losing the game. The King can make 1 move in any direction and can take 2 steps to 'castle' if the Rook involved
            in the castling has yet to move. The King must also not have moved prior to the castle. Castles can not occur when in check.

        @param played: Indicates whether the King has moved or not.
        @param possibleMoves: A set of all the possible moves the King can make.
    """

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, "K", "\u2654",  900, x, y, board)

        if self.team == "W":
            self.icon = "\u265A"

        self.played = False
        self.possibleMoves = [[0, 1], [0, -1], [1, 0], [1, 1],
                              [1, -1], [-1, 0], [-1, 1], [-1, -1], [2, 0], [-2, 0]]

    # Check Piece.py documentation for more information regarding this method.
    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x, y):
            return False

        possibleMoves = self.getMoveSet(self.possibleMoves)

        xDifference = x - self.x
        yDifference = y - self.y

        if xDifference == possibleMoves[0][0]:

            if yDifference == possibleMoves[0][1]:
                return True
            elif yDifference == possibleMoves[1][1]:
                return True
            else:
                return False

        elif xDifference == possibleMoves[2][0]:

            if yDifference == possibleMoves[2][1]:
                return True
            elif yDifference == possibleMoves[3][1]:
                return True
            elif yDifference == possibleMoves[4][1]:
                return True
            else:
                return False

        elif xDifference == possibleMoves[5][0]:

            if yDifference == possibleMoves[5][1]:
                return True
            elif yDifference == possibleMoves[6][1]:
                return True
            elif yDifference == possibleMoves[7][1]:
                return True
            else:
                return False

        # The last two elif's determine if castling is allowed.
        elif xDifference == possibleMoves[8][0]:

            if yDifference == possibleMoves[8][1]:

                if self.board.isEmpty(self.x + possibleMoves[8][0], self.y):
                    return True
            else:
                return False

        elif xDifference == possibleMoves[9][0]:

            if yDifference == possibleMoves[9][1]:

                if self.board.isEmpty(self.x + possibleMoves[9][0], self.y):
                    return True

        else:
            return False

    # Check Piece.py documentation for more information regarding this method.
    def update(self, x: int, y: int) -> bool:

        if self.validMove(x, y):

            # Determine if castling is allowed.
            if x - self.x == 2:
                if type(self.board.board[self.y][7]) is Rook and not self.board.board[self.y][7].played:
                    # Update Rook's position.
                    self.board.board[self.y][7].update(5, self.y)
                else:
                    print("Cannot castle since pieces have already moved.")
                    return False

            if x - self.x == -2:
                if type(self.board.board[self.y][0]) is Rook and not self.board.board[self.y][0].played:
                    # Update Rook's position.
                    self.board.board[self.y][0].update(3, self.y)
                else:
                    print("Cannot castle since pieces have already moved.")
                    return False

            self.played = True
            self.move(x, y)
            return True
        else:
            print("Illegal move. Try again.")
            return False
