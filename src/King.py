from Piece import Piece
from Utility import *
from Rook import Rook

class King(Piece):

    def __init__(self, team, board, x, y):
        super().__init__("k", team, board, x, y)
        self.castleAttempt = False
        
    def isValidMove(self, move: str) -> bool:

        intMove = Utility.convertStringMoveToInt(move)
        newX = intMove[2]
        newY = intMove[3]

        xDifference = newX - self.x
        yDifference = newY - self.y

        if [xDifference, yDifference] in self.basicMoves:

            if self.played == False and abs(xDifference) == 2:
                if xDifference == 2:
                    if self.board.isEmpty(7, self.y) == False and type(self.board.board[self.y][7]) is Rook:
                        moveAttempt = Utility.convertIntMoveToString([self.x, self.y, 6, self.y])
                        if self.board.board[self.y][7].played == False and self.isValidPath(moveAttempt):
                            self.castleAttempt = True
                            return True
                elif xDifference == -2:
                    if self.board.isEmpty(0, self.y) == False and type(self.board.board[self.y][0]) is Rook:
                        moveAttempt = Utility.convertIntMoveToString([self.x, self.y, 1, self.y])
                        if self.board.board[self.y][0].played == False and self.isValidPath(moveAttempt):
                            self.castleAttempt = True
                            return True
                else:
                    return False
            elif self.isValidPath(move):
                return True
            elif self.board.isEmpty(newX, newY) == True or self.board.canAttack(newX, newY, self.team):
                return True
            else:
                return False

        return False

    def move(self, move: str) -> bool:

        if move in self.possibleMoves:
            intMove = Utility.convertStringMoveToInt(move)
            currentX = intMove[0]
            currentY = intMove[1]
            newX = intMove[2]
            newY = intMove[3]
            self.board.removePiece(currentX, currentY)
            self.updateCounter(newX, newY)
            self.board.addPiece(self, newX, newY)
            self.x = newX
            self.y = newY

            if self.castleAttempt == True:

                if newX > 4:
                    self.board.board[self.y][5] = self.board.board[self.y][7]
                    self.board.removePiece(7, self.y)
                if newX < 4:
                    self.board.board[self.y][3] = self.board.board[self.y][0]
                    self.board.removePiece(0, self.y)
                
                self.castleAttempt = False

            if self.played == False:
                self.played = True
            
            self.board.lastMove = self.name + move
        else:
            print(move + " " + "is an illegal move. Try again")
            return False