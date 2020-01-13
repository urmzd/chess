from Piece import Piece


class Pawn(Piece):

    """
        Note: Inherits properties from Piece, check Piece.py for more information about attributes.
        @desc: Represents a Pawn piece in the game of Chess. The Pawn is allowed 2 moves forward on the first turn, 1 move in the forward direction otherwise.
            It is allowed to attack diagonally but only 1 unit diagonally. It can also the use the En Passent rule to remove a piece behind it,
            given that the last move made was by the enemy Pawn moving two units towards the current Pawn.

        @param possibleMoves: A set of all possible moves the Pawn can make.
        @param played: Indicates if played already. Default = False.
        @param enPassent: Indicates if En Passent can be used or not. Default = False.
    """

    def __init__(self, team: chr, x: int, y: int, board: "Board"):
        super().__init__(team, "P", "\u2659", -10, x, y, board)

        if self.team == "W":
            self.icon = "\u265F"
            self.value = abs(self.value)

        self.possibleMoves = [[0, 1], [0, 2], [1, 1], [-1, 1]]
        self.played = False
        self.enPassent = False

    # Check Piece.py for more documentation.
    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x, y):
            return False

        # Determine the correct set of possible moves. Invert if necessary.
        possibleMoves = self.getMoveSet(self.possibleMoves)

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

            # Checks if an attack can be made.
            if yDifference == possibleMoves[2][1]:
                if not self.board.isEmpty(x, y) and not self.isFriendly(x, y):
                    return True

                # Checks if En Passent can be used or not.
                elif self.board.isEmpty(x, y):
                    
                    lastMove = self.board.lastMove

                    if lastMove != "" and lastMove[1] == "P":
                        if int(lastMove[2]) + 1 == self.x or int(lastMove[2]) - 1 == self.x:
                            if abs(int(lastMove[3]) - int(lastMove[5])):
                                self.enPassent = True
                                return True
                else:
                    return False

        else:
            return False

    # Check Piece.py for more documentation.
    def update(self, x: int, y: int) -> bool:

        if self.validMove(x, y):

            # If En Passent is allowed, determine which way the piece is facing and remove the piece behind it.
            if self.enPassent:
                if self.team == "W":
                    self.capture(x, y - 1)
                else:
                    self.capture(x, y + 1)
                self.enPassent = False

            if self.played == False:
                self.played = True

            # Reset the 50-move rule counter since a pawn move has been made.
            self.board.resetCounter()
            self.move(x, y)

            if y == 0 or y == 7:
                self.requestUpgrade()

            return True
        else:
            print("Illegal move. Try again.")
            return False

    # Calls upgrade in the board class.
    def requestUpgrade(self):

        pieceType = input(
            "Please enter the lowercase letter of the piece you would like to upgrade to: ")

        while not self.board.promotePawn(pieceType, self.team, self.x, self.y):
            pieceType = input(
                "Please enter the lowercase letter of the piece you would like to upgrade to: ")
