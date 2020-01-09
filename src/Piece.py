class Piece:

    def __init__(self, name, color, x, y, board):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.board = board

    def difference(self, a, b):
        return abs(a - b)

    def update(self, x, y):
        board[x][y].x = x
        board[x][y].y = y
        board[x][y] = self

    def capture(self, x, y):
        if not isFriendly(x, y):
            self.board[x][y] = None
        else:
            print("Invalid move! Friendly piece exists at coordinate specified.")
    
    def isFriendly(self, x, y):
        return True if self.board[x][y].color == self.color else False

    def isEmpty(self, x, y):
        return True if self.board[x][y] == None else False

    def storeMove(self, x, y):
        self.board.lastMove = self.color + self.name + self.x + self.y + x + y

    def isWithinBounds(self, x, y):
        return True if x >= 1 and x <= 8 and y >= 1 and y <= 8 else False

    def isValidMove(self, x, y):
        pass

    def isValidPath(self, x, y):
        pass

    def move(self, x, y):
        pass