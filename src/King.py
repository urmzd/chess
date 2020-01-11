from typing import List
from Piece import Piece

class King(Piece):

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, "K", "\u2654",  1000, x, y, board)
        self.played = False

    def validMove(self, x: int, y: int) -> bool:
        
        if not self.validPosition(x,y):
            return False

        if abs(x - self.x) > 1 and abs(y - self.y) > 1:
            return False
        
        if not self.played:

            if abs(y - self.y) == 0:
                if abs(x - self.x) == 2:
                    for step in range(1, abs(x - self.x)):
                        if not self.board.isEmpty(self.x + step, self.y):
                            return False
                    if not self.board.board[self.y][7].played:
                        return True

            if x - self.x == -2:
                for step in range(1, abs(x - self.x)):
                    for step in range(1, abs(x - self.x) + 1):
                        if not self.board.isEmpty(self.x - step, self.y):
                            return False
                    if not self.board.board[self.y][0].played:
                        return True

        return False
    
    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            
            if x - self.x == 2:
                self.board.board[self.y][7].update(5, self.y)

            if x - self.x == -2:
                self.board.board[self.y][0].update(3, self.y)

            self.played = True
            self.move(x, y)

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass