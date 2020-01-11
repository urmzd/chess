from typing import List
from Piece import Piece

class Rook(Piece):

    def __init__(self, color, x, y, board):
        super().__init__("R", color, 5, x, y, board)
        self.played = False
        
    # @Override
    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            if not self.board.isEmpty(x, y):
                if not self.board.isFriendly(x, y, team):
                    self.board.board[y][x].capture(x, y)
            else:
                self.move(x, y)
        else:
            print("Invalid move.")

    def validMove(self, x: int, y: int) -> bool:
        
        validMove = False

        if self.board.isEmpty(x,y):
            return True
        
        if self.board.isFriendly(x, y, self.team):
            return False
        else:
            return True

        if abs(x - self.x) == 0:
            for step in range(1, abs(y - self.y)):
                if not self.board.isEmpty(x, y + step):
                    return False
            if self.board.isEmpty(x, y) or not self.board.isFriendly(x, y, self.team):
                validMove = True
        
        if abs(y - self.y == 0):
            for step in range(1, abs(x - self.x)):
                if not self.board.isEmpty(x + step, y):
                    return False

            if self.board.isEmpty(x, y) or not self.board.isFriendly(x, y, self.team):
                validMove = True

        return validMove

    def getPossibleMoves(self) -> List[List[int]]:
        pass