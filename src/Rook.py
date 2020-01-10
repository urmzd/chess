from Piece import Piece

class Rook(Piece):

    def __init__(self, color, x, y, board, played):
        super().__init__("R", color, 5, x, y, board)
        self.played = False