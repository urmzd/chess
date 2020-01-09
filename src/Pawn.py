import Piece

class Pawn(Piece):

    def __init__(self, name, color, x, y, board, played):
        super().__init__(name, color, x, y, board, False)

    def isCorrectDirection(self, y):
        
        if self.color == 'W':
            if y > self.y:
                return True
        else:
            if y < self.y:
                return True
        
        return False
    
    def allowedEnPassent(self):

        lastMove = self.board.lastMove

        if not isEmpty(x, y):
            return False

        if lastMove[1] == "P":
            if int(lastMove[3]) - 1 == self.x or int(lastMove[3]) + 1 == self.x:
                if lastMove[0] == "B":
                    if lastMove[2] == "g":
                        if lastMove[4] == "e":
                            return True
                else:
                    if lastMove[2] == "b":
                        if lastMove[4] == "d":
                            return True
        return False

    def isValidPath(self, x, y):

        for step in range(self.difference(y, self.y)):
            if not self.isEmpty(x, y + step):
                return False

        return True

    def isValidMove(self, x, y):
        
        if not self.isCorrectDirection(y) or not self.isWithinBounds(x,y):
            return False

        if self.difference(x, self.x) == 0:
            if not self.played and self.isValidPath(x,y) and self.difference(y, self.y) == 2:
                return True
            if self.isEmpty(x,y) and self.difference(y, self.y) == 1 and :
                return True

        if self.difference(x, self.x) == 1 and self.difference(y, self.y) == 1:

            if self.allowedEnPassent() and x == int(self.board.lastMove[3]):
                return True

            if not self.isEmpty(x,y) and not self.isFriendly(x,y):
                return True
    

        return False

    def move(self, x, y):
        
        if self.isValidMove(x,y):

            if self.played == False:
                self.played = True

            self.storeMove(x, y):
                if self.allowedEnPassent(x, y):
                    if self.color == "W":
                        self.capture(x, y - 1)
                    else:
                        self.capture(x, y + 1)
                else:
                    self.capture(x, y)

            self.update(x, y)