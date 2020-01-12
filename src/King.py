from Piece import Piece
from Rook import Rook


class King(Piece):

    possibleMoves = [[0, 1], [0, -1], [1, 0], [1, 1],
                     [1, -1], [-1, 0], [-1, 1], [-1, -1], [2, 0], [-2, 0]]

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, "K", "\u2654",  900, x, y, board)
        self.played = False

        if self.team == "W":
            self.icon = "\u265A"

    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x, y):
            return False

        if not self.updated:
            possibleMoves = self.getMoveSet(self.possibleMoves)
        else:
            possibleMoves = self.possibleMoves

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

    def update(self, x: int, y: int) -> bool:

        if self.validMove(x, y):

            if x - self.x == 2:
                if isinstance(self.board.board[self.y][7], Rook):
                    self.board.board[self.y][7].update(5, self.y)

            if x - self.x == -2:
                if isinstance(self.board.board[self.y][0], Rook):
                    self.board.board[self.y][0].update(3, self.y)

            self.played = True
            self.move(x, y)

        else: 
            print("Illegal move. Try again.")