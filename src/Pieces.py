class Piece:

    def __init__(self, name, color, x, y, board):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.board = board

    # Converts char to int.
    def convertY(self, y):
        return ord(chr(y)) - 96

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
        else:
            if y < self.y:
                return True
        
        return False
    
    ## Checks if opposing pawn moved two steps on left or right side.
    def allowedEnPassent(self):

        # Ex: WPb2d2, BPg2e2
        # Check Colour: W (B), B (G)
        # Convert B to 2
        # Convert D to 4
        # Convert G to 7
        # Convert E to 5
        # Subtract abs(D - B) = 2 (En Passent Allowed) for Any Pawn on (1, D) or (3, D)
        # Subtract abs(G - E) = 2 (En Passent Allowed) for Any Pawn on (1, E) or (3, E)
        lastMove = self.board.lastMove

        if lastMove[1] == "P":
            if int(lastMove[3]) - 1 == self.x or int(lastMove[3]) + 1 == self.x:
                if lastMove[0] == "B":
                    if lastMove[2] == "g":
                        if lastMove[4] == "e":
                            return True
                else:
                    if lastMove[2] == "b":
                        if lastMove[4] == "e":
                            return True
        return False


    # if not played, can move 2 spots in the y direction.
    # if moved only spot is allowed.
    # only diagonal attacks are allowed. Check if enemy exists on (1,1) on either side.
    # An "en passent" can be made if the opponent moves two units to prevent being captured AND
    ## NO OTHER MOVE HAS BEEN MADE SINCE THEN.
    def isValidMove(self, x, y):
        
        if not self.isCorrectDirection(y):
            return False
        
        if not self.played and abs(x - self.x) == 0:
            if abs(y - self.y) == 2:
                return True

        if self.allowedEnPassent() and abs(self.x - x) == 1 and abs(self.y - y) == 1 and x == int(self.board.lastMove[3]):
            return True

        if not self.isEmpty(x,y) and abs(self.x - x) == 1 and abs(self.y - y) == 1 and not self.isFriendly(x,y):
            return True

        if abs(self.y - y) == 1 and abs(self.x - x) == 0 and self.isEmpty(x,y):
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
