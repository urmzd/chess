from typing import List
from Piece import Piece

class Queen(Piece):

    def __init__(self, team: chr, x: int, y: int, board: "Board"):
        super().__init__(team, "Q", "\u2655",  9, x, y, board)

    def validMove(self, x: int, int: int) -> bool:
        pass
    
    def update(self, x: int, y: int):
        pass

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass