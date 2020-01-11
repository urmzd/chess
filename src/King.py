from typing import List
from Piece import Piece
from Rook import Rook

class King(Piece):

    def __init__(self, color, x, y, board):
        super().__init__("K", color, 100, x, y, board)
        self.played = False

    def validMove(self, x: int, y: int):
        
        # Regular move set.
        if x <= 1 and y <= 1:
            if self.board.isEmpty(x, y) or not self.board.isFriendly(x, y, self.team):
                return True
        
        # For castling
        if not self.played and abs(y - self.y) == 0:
            if abs(x - self.x) == 2 or abs(x - self.x) == 3:

                for step in range(1, abs(x - self.x)):

                    if abs(x - self.x) == 3:
                        step = -step

                    if not self.board.isEmpty(self.x + step, y):
                        return False

                if abs(x - self.x) == 2:
                    if isinstance(self.board.board[self.y][7], Rook):
                        if not self.board.board[self.y][7].played:
                            return True

                if abs(x - self.x) == 3:
                    if isinstance(self.board.board[self.y][0], Rook):
                        if not self.board.board[self.y][0].played:
                            return True

        return False

    def update(self, x: int, y: int):

        if self.validMove(x, y):
            if x <= 1 and y <= 1:
                if not self.board.isFriendly(x, y, self.team):
                    self.capture(x, y)
                    self.move(x, y)

            if abs(x - self.x) == 2:
                self.board.update(7, self.y, 5, self.y)
                self.move(6, self.y)
            
            if abs(x - self.x) == 3:
                self.board.update(0, self.y, 3, self.y)
                self.move(2, self.y)
            
            self.played = True
        else:
            print("Invalid move, try again.")
            

    def getPossibleMoves(self):
        pass