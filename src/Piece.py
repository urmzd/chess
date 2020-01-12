from typing import List

class Piece():

    def __init__(self, team: chr, name: chr, icon: chr, value: int, x: int, y: int, board: "Board", possibleMoves = [[]]):
        self.team = team
        self.name = name
        self.icon = icon
        self.value = value
        self.x = x
        self.y = y
        self.board = board
        self.possibleMoves = possibleMoves
    
    def move(self, x: int, y: int):
        self.storeMove(x,y)

        if not self.board.isEmpty(x,y):
            self.capture(x, y)
            self.board.resetCounter()

        self.board.board[y][x] = self
        self.board.board[self.y][self.x] = None
        self.x = x
        self.y = y

    def capture(self, x: int, y: int):
        self.board.remove(x, y)
    
    def isFriendly(self, x: int, y: int) -> bool:        
        return self.team == self.board.board[y][x].team

    def validPosition(self, x: int, y: int) -> bool:
        if not self.board.contains(x,y):
            return False

        return self.board.isEmpty(x, y) or not self.isFriendly(x, y)
    
    def getMoveSet(self) -> List[List[int]]:
        moves = self.possibleMoves

        if self.team == "B":
            for moveset in range(len(moves)):
                for move in range(len(moves[moveset])):
                    moves[moveset][move] = -moves[moveset][move]

        return moves
    
    def storeMove(self, x: int, y: int):
        self.board.lastMove = self.team + self.name + str(self.x) + str(self.y) + str(x) + str(y)
    
    def __repr__(self):
        return self.icon

    def validMove(self, x: int, int: int) -> bool:
        pass
    
    def update(self, x: int, y: int):
        pass

    # DEFAULT FOR KING, PAWN AND KNIGHT. QUEEN, BISHOP AND ROOK WILL HAVE THEIR OWN IMPLEMENTATION.
    def getAllPossibleMoves(self) -> List[List[int]]:

        possibleMoves = self.getMoveSet(self.possibleMoves, self.team)
        validMoves = []

        for move in self.possibleMoves:
            if self.validMove(move[0], move[1]):
                validMoves.append(move)
            
        return validMoves