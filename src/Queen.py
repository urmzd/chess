from typing import List
from Piece import Piece
from Rook import Rook
from Bishop import Bishop

class Queen(Piece):

    def __init__(self, team: chr, x: int, y: int, board: "Board"):
        super().__init__(team, "Q", "\u2655",  9, x, y, board)
        if self.team == "W":
            self.icon = "\u265B"

    def validMove(self, x: int, y: int) -> bool:
        
        bishop = Bishop(self.team, self.x, self.y, self.board)
        rook = Rook(self.team, self.x, self.y, self.board)

        if bishop.validMove(x, y) or rook.validMove(x, y):
            return True
        
        return False
    
    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            self.move(x, y)

    def getAllPossibleMoves(self) -> List[List[int]]:
        
        validMoves = []

        bishop = Bishop(self.team, self.x, self.y, self.board)
        rook = Rook(self.team, self.x, self.y, self.board)

        for move in bishop.getAllPossibleMoves():
            validMoves.append(move)
        
        for move in rook.getAllPossibleMoves():
            validMoves.append(move)

        return validMoves