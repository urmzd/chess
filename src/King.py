from typing import List
from Piece import Piece

class King(Piece):

    def __init__(self, team: chr, x: int, y: int, board: 'Board'):
        super().__init__(team, "K", "\u2654",  1000, x, y, board)
        self.played = False

    def validMove(self, x: int, y: int) -> bool:

        if not self.validPosition(x,y):
            return False

        possibleMoves = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1], [2, 0], [-2, 0]]
        
        self.inverseMoveSet(possibleMoves, self.team)

        xDifference = x - self.x
        yDifference = y - self.y

        if xDifference == possibleMoves[0][0]:

            if yDifference == possibleMoves[0][1]:
                return True
            elif yDifference == possibleMoves[1][1]:
                return True
            else:
                return False

        elif xDifference == possibleMoves[2][0]:

            if yDifference == possibleMoves[2][1]:
                return True
            elif yDifference == possibleMoves[3][1]:
                return True
            elif yDifference == possibleMoves[4][1]:
                return True
            else:
                return False

        elif xDifference == possibleMoves[5][0]:

            if yDifference == possibleMoves[5][1]:
                return True
            elif yDifference == possibleMoves[6][1]:
                return True
            elif yDifference == possibleMoves[7][1]:
                return True
            else:
                return False

        elif xDifference == possibleMoves[8][0]:
             
            if yDifference == possibleMoves[8][1]:

                 if self.board.isEmpty(self.x + possibleMoves[8][0], self.y):
                     return True
            else:
                return False

        elif xDifference == possibleMoves[9][0]:
            
            if yDifference == possibleMoves[9][1]:

                if self.board.isEmpty(self.x + possibleMoves[9][0], self.y):
                    return True

        else:
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