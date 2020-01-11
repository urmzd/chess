from typing import List
from Piece import Piece

class Rook(Piece):

    def __init__(self, team: str, x: int, y: int, board: "Board"):
        super().__init__(team, "R", "\u2656", 5, x, y, board)
        self.played = False

    def validMove(self, x: int, int: int) -> bool:
        pass
    
    def update(self, x: int, y: int):
        pass

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass