from typing import List
from Piece import Piece

class Rook(Piece):

    def __init__(self, team: str, x: int, y: int, board: "Board"):
        super().__init__(team, "R", "\u2656", 5, x, y, board)
        self.played = False

    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x, y):
            return False

        if abs(self.x - x) == 0:

            for step in range(1, abs(self.y - y)):
                if y - self.y < 0:
                    step = -step

                if not self.board.isEmpty(self.x, self.y + step):
                    return False
                return True
        
        if abs(self.y - y) == 0:
            
            for step in range(1, abs(self.x - x)):

                if x - self.x < 0:
                    step = -step

                if not self.board.isEmpty(self.x + step, self.y):
                    return False
                return True

        return False
    
    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            self.move(x, y)

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass