from Piece import Piece


class Pawn(Piece):

    def __init__(self, team: chr, x: int, y: int, board: "Board"):
        super().__init__(team, "P", "\u2659", 10, x, y, board)

        if self.team == "W":
            self.icon = "\u265F"

        self.possibleMoves = [[0, 1], [0, 2], [1, 1], [-1, 1]]
        self.played = False
        self.enPassent = False

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

            elif yDifference == possibleMoves[1][1] and not self.played:

                if not self.board.isEmpty(x, self.y + possibleMoves[1][1]):
                    return False

                return True
            else:
                return False

        elif xDifference == possibleMoves[2][0] or xDifference == possibleMoves[3][0]:

            if yDifference == possibleMoves[2][1]:
                if not self.board.isEmpty(x, y) and not self.isFriendly(x, y):
                    return True

                elif self.board.isEmpty(x, y):
                    lastMove = self.board.lastMove
                    if lastMove[1] == "P":
                        if int(lastMove[2]) + 1 == self.x or int(lastMove[2]) - 1 == self.x:
                            if abs(int(lastMove[3]) - int(lastMove[5])):
                                self.enPassent = True
                                return True
                else:
                    return False

        else:
            return False

    def update(self, x: int, y: int) -> bool:

        if self.validMove(x, y):

            if self.enPassent:
                if self.team == "W":
                    self.capture(x, y - 1)
                else:
                    self.capture(x, y + 1)
                self.enPassent = False

            if self.played == False:
                self.played = True

            self.board.resetCounter()
            self.move(x, y)
            return True
        else:
            print("Illegal move. Try again.")
            return False
