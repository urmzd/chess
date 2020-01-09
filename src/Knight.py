from Piece import Piece

class Knight(Piece):

    def __init__(self, color, x, y, board):
        super().__init__("N", color, 3, x, y, board)