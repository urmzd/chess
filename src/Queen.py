from typing import List
from Piece import Piece
from Rook import Rook
from Bishop import Bishop


class Queen(Piece):

    """
        Note: Inherits properties from Piece, check Piece.py for more information about attributes.
        @desc: Represent a Queen in the game of Chess. The Queen is a mix between the Bishop and the Rook.
            It can take any number of steps in any direction.
    """
    def __init__(self, team: chr, x: int, y: int, board: "Board"):
        super().__init__(team, "Q", "\u2655",  90, x, y, board)

        if self.team == "W":
            self.icon = "\u265B"
    
    # Refer to Piece.py documentation for more information about this piece.
    def validMove(self, x: int, y: int) -> bool:

        bishop = Bishop(self.team, self.x, self.y, self.board)
        rook = Rook(self.team, self.x, self.y, self.board)

        ## If a 'ghost' bishop or rook can make the move, the move is considered legal.
        if bishop.validMove(x, y) or rook.validMove(x, y):
            return True

        return False
        
    # Refer to Piece.py documentation for more information about this piece.
    def update(self, x: int, y: int) -> bool:

        if self.validMove(x, y):
            self.move(x, y)
        else:
            print("Illegal move. Try again.")
            return False

    # Refer to Piece.py documentation for more information about this piece.
    def getAllPossibleMoves(self) -> List[List[int]]:

        validMoves = []

        bishop = Bishop(self.team, self.x, self.y, self.board)
        rook = Rook(self.team, self.x, self.y, self.board)

        ## The possible moves are the union of all valid moves from a 'ghost' bishop and rook.
        for move in bishop.getAllPossibleMoves():
            validMoves.append(move)

        for move in rook.getAllPossibleMoves():
            validMoves.append(move)

        return validMoves
