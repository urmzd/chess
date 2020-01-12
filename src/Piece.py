from typing import List

class Piece():

    def __init__(self, team: chr, name: chr, icon: chr, value: int, x: int, y: int, board: "Board"):
        self.team = team
        self.name = name
        self.icon = icon
        self.value = value
        self.x = x
        self.y = y
        self.board = board
    
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
        if not self.board.isContained(x,y):
            return False

        return self.board.isEmpty(x, y) or not self.isFriendly(x, y)
    
    @classmethod
    def inverseMoveSet(cls, list, team):
        if team == "B":
            for moveset in range(len(list)):
                for move in range(len(list[moveset])):
                    list[moveset][move] = -list[moveset][move]
    
    def storeMove(self, x: int, y: int):
        self.board.lastMove = self.team + self.name + str(self.x) + str(self.y) + str(x) + str(y)
    
    def __repr__(self):
        return self.icon

    def validMove(self, x: int, int: int) -> bool:
        pass
    
    def update(self, x: int, y: int):
        pass

    def getPossibleMoves(self, x: int, y: int) -> List[List[int]]:
        pass