class Piece:

    def __init__(self, name, color, x, y, board):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.board = board

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
    def isValid(self, x, y):
        pass
    
    ## Checks if friendly exists at (x, y)
    def isFriendly(self, x, y):
        return True if self.board[x][y].color == self.color else False

    ## Check if spot is empty.
    def isEmpty(self, x, y):
        return True if self.board[x][y] == None else False

    ## Stores last move made. Used for en passent.
    def storeMove(self):
        self.board.lastMove = str(name) + str(color) + str(x) + str(y)

    ## Checks if move will let piece stay within board.
    def isWithinBounds(self, x, y):
        return True if x >= 1 and x <= 8 and y >= 1 and y <= 8 else False

'''
    Methods:

        Move(x,y):
            1. Can only move 1 unit in the y direction after the initial move.
            2. The initial action can consist of moving 2 units in the y direction.
            3. The Pawn can use an 'en passent' which initially allows it to move
                1 unit in the x direction and 1 unit in the y direction if the enemy pawn
                attempts to save itself by moving 2 units in the y direction using it's 
                initial action. This move can only be made immediately after the enemy makes a two step move.
                Otherwise, this right is lost.
            4. The pawn can capture other pieces diagonally (1 unit in the positive x and y direction).
'''
class Pawn(Piece):

    def __init__(self, name, color, x, y, board, played):
        super().__init__(name, color, x, y, board, False)

    ## Determines if pawn piece is only going forward/ backward (Depending on colour).
    def isCorrectDirection(self, y):
        
        if self.color == 'W':
            if y > self.y:
                return True

        if self.color == 'B':
            if y < self.y:
                return True
        
        return False

    # if not played, can move 2 spots in the y direction.
    # if moved only spot is allowed.
    # only diagonal attacks are allowed. Check if enemy exists on (1,1) on either side.
    # An "en passent" can be made if the opponent moves two units to prevent being captured AND
    ## NO OTHER MOVE HAS BEEN MADE SINCE THEN.
    def isValid(self, x, y):
        
        if not self.played and abs(x - self.x) == 0:
            if not isCorrectDirection(y) and abs(y - self.y) == 2:
                return True
        
        return False

    def move(self, x,y):
        pass

    
class King(Piece):

    def __init__(self, name, color, x, y, board):
        super().__init__(name, color, x, y, board)

class Queen(Piece):

    def __init__(self, name, color, x, y, board):
        super().__init__(name, color, x, y, board)

class Knight(Piece):

    def __init__(self, name, color, x, y, board):
        super().__init__(name, color, x, y, board)

class Rook(Piece):

    def __init__(self, name, color, x, y, board):
        super().__init__(name, color, x, y, board)

class Bishop(Piece):

    def __init__(self, name, color, x, y, board):
        super().__init__(name, color, x, y, board)