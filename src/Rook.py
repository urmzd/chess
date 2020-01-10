from Piece import Piece
from King import King

class Rook(Piece):

    KING_SIDE_CASTLE = 5
    QUEEN_SIDE_CASTLE = 3

    def __init__(self, color, x, y, board, played):
        super().__init__("R", color, 5, x, y, board)
        self.played = False
    
    def isValidPath(self, x, y):
        
        if difference(x, self.x) == 0:
            
            for step in range(difference(y, self.y)):
                if not self.isEmpty(x, y + step):
                    return False
            
        if difference(y, self.y) == 0:
            
            for step in range(difference(x, self.x)):
                if not self.isEmpty(x + step, y):
                    return False

        return True
    
    def castle():

        tempY = 0 # Default set for White.

        if self.color == "B":
            y = 7

        if x == 0:
            self.move(self.QUEEN_SIDE_CASTLE, y)
        if x == 7:
            self.move(self.KING_SIDE_CASTLE, y)

    def isValidMove(self, x, y):
        
        if difference(x, self.x) == 0:
            if isValidPath(x, y):
                return True
        
        if difference(y, self.y) == 0:
            if isValidPath(x, y):
                return True

        return False


    def move(self, x, y):
        
        if isValidMove(x,y):
            self.update(x,y)