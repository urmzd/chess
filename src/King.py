from Piece import Piece

class King(Piece):

    def __init__(self, color, x, y, board):
        super().__init__("K", color, 100, x, y, board)