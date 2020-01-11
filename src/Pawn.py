from typing import List
from Piece import Piece

class Pawn(Piece):

    def __init__(self, team: chr, x: int, y: int, board: "Board"):
        super().__init__(team, "P", "\u2659", 1, x, y, board)
        self.played = False
        self.enPassent = False

    def validMove(self, x: int, y: int) -> bool:
  
        if self.team == "W":
            step = 1
            if y < self.y:
                return False

        if self.team == "B":
            step = -1
            if y > self.y:
                return False

        if abs(self.x - x) > 1 or abs(self.y - y) > 2:
            return False
        
        if not self.validPosition(x, y):
            return False
        
        if abs(self.x - x) == 0:
            if abs(self.y - y) == 2:
                if self.validPosition(self.x, self.y + step):
                    return True
            if abs(self.y - y) == 1:
                return True

        if abs(self.y - y) == 1 and abs(self.x - x) == 1:


            if not self.board.isEmpty(x,y) and not self.isFriendly(x, y):
                return True

            lastMove = self.board.lastMove

            if lastMove[1] == "P":
                if int(lastMove[2]) + 1 == self.x or int(lastMove[2]) - 1 == self.x:
                    if abs(int(lastMove[3]) - int(lastMove[5])) == 2:
                        self.enPassent = True
                        return True
        
        return False
            
    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            
            if self.enPassent:
                if self.team == "W":
                    self.capture(x, y - 1) 
                else:
                    self.capture(x, y + 1)
            
            if self.played == False:
                self.played = True
                
            self.board.incrementCounter()
            self.move(x, y)

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass