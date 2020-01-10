from typing import List
from Piece import Piece
 
class Pawn(Piece):

    def __init__(self, team, x, y, board):
        super().__init__("P", team, 1, x, y, board)
        self.played = False
    
    def isValidPath(self, x: int, y: int) -> bool:
        pass

    def isValidMove(self, x: int, y: int) -> bool:
        pass

    def getPossibleMoves(self) -> List[List[int]]