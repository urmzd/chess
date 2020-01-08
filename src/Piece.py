class Piece:

    def __init__(self, name, color, x, y, board):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.board = board

    # Returns the absolute difference between two values.
    def difference(self, a, b):
        return abs(a - b)

    ## moves piece on board.
    def move(self, x, y):
        pass

    # Helper method.
    ## Removes piece at given coordinate (x,y)
    def capture(self, x, y):
        if not isFriendly(x, y):
            self.board[x][y] = None
        else:
            print("Invalid move! Friendly piece exists at coordinate specified.")

    # Helper method.
    # Checks if move made is valid
    ## First it checks if pieces are blocking its path.
    ## Next it checks if a friendly piece already exists at the spot.
    ## Additionally, only the knight can hop over other pieces,
    ## So this method will be implemented differently for every piece.
    def isValidMove(self, x, y):
        pass
    
    ## Checks if friendly exists at (x, y)
    def isFriendly(self, x, y):
        return True if self.board[x][y].color == self.color else False

    ## Check if spot is empty.
    def isEmpty(self, x, y):
        return True if self.board[x][y] == None else False

    ## Stores last move made. Used for en passent.
    def storeMove(self, x, y):
        self.board.lastMove = self.color + self.name + self.x + self.y + x + y

    ## Checks if move will let piece stay within board.
    def isWithinBounds(self, x, y):
        return True if x >= 1 and x <= 8 and y >= 1 and y <= 8 else False