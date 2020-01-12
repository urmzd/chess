from Board import Board


class Player:

    def __init__(self, board):
        self.board = board
        self.inCheck = False
        self.lost = False
        self.worth = None

    def isInCheck(self):
        # Get position of King
        # Check if position of King is a valid move for all pieces on the current team
        # If it is, this player is inCheck
        pass

    def updateWorth(self):
        # Get value of all pieces.
        # Get value of all positions.
        # worth = value of all pieces + value of postions the pieces are on.
        pass

    def movePiece(self, move: str):
        self.board.update(move)
