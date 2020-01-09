from Piece import Piece

        
class Queen(Piece):

    def __init__(self, color, x, y, board):
        super().__init__("Q", color, 9, x, y, board)