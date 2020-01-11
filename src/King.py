from typing import List
from Piece import Piece

class King(Piece):

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, "K", "\u2654",  1000, x, y, board)
        self.played = False

    def validMove(self, x: int, y: int) -> bool:
        pass
    
    def update(self, x: int, y: int):
        pass

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass