from typing import List
from Piece import Piece

class Bishop(Piece):

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, 'B', "\u2657", 3, x, y, board)

    def validMove(self, x: int, y: int) -> bool:
        pass
    
    def update(self, x: int, y: int):
        pass

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass