from Piece import Piece

class Knight(Piece):

    def __init__(self, team: chr, x: int, y: int, board: "Board"):
        super().__init__(team, "N", "\u2658", 3, x, y, board)
        self.possibleMoves = possibleMoves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        if self.team == "W":
            self.icon = "\u265E"

    def validMove(self, x: int, y: int) -> bool:
                
        if not self.validPosition(x, y):
            return False

        possibleMoves = self.getMoveSet()

        xDifference = self.x - x
        yDifference = self.y - y

        if xDifference == 1:
            if yDifference == 2:
                return True
            if yDifference == -2:
                return True
        elif xDifference == -1:
            if yDifference == 2:
                return True
            if yDifference == -2:
                return True
        elif xDifference == 2:
            if yDifference == -1:
                return True
            if yDifference == 1:
                return True
        elif xDifference == -2:
            if yDifference == -1:
                return True
            if yDifference == 1:
                return True
        else:
            return False

    def update(self, x: int, y: int):
        
        if self.validMove(x,y):
            self.move(x, y)