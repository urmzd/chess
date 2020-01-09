from Piece import Piece

class Bishop(Piece):

    def __init__(self, color, x, y, board):
        super().__init__("B", color, 3, x, y, board)
