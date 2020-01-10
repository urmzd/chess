"""
    @desc: The Piece class is meant to be a class which all pieces in the 
    Chess game are to inherit the properties of. It also contains helper methods
    meant to reduce the number of lines written in each child class.
"""
class Piece:

    """
        @desc: A constructor to initialize basic attributes all children of this class will inherit.
        @param name: A single character representation of the piece name. Ex: "P" for Pawn.
        @param color: A single character representation of the piece team. "W" for White, "B" for Black.
        @param value: An integer representing the value of the piece.
        @param x: An integer indicating the x position of the piece.
        @param y: An integer indiciating the y position of the piece.
        @param board: The board in which the piece will move on.
    """
    def __init__(self, name, color, value, x, y, board):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.board = board

    """
        @desc: difference is a method that returns the difference in values. 
        @param a: The starting value.
        @param b: The ending value.
        @return int: The absolute difference between two integers.
    """
    def difference(self, a, b):
        return abs(a - b)

    """
        @desc: update is a method that updates the board and the piece with a new position.
        @param x: The new X position of the piece.
        @param y: The new Y position of the piece.
    """
    def update(self, x, y):
        self.board.board[y][x] = self
        self.board.board[self.y][self.x] = None
        self.board.board[y][x].x = x
        self.board.board[y][x].y = y
        
    """
        @desc: capture removes piece at given coordinate in the format: (x,y)
        @param x: The x coordinate in which to remove the piece. 
        @param y: The y coordinate in which to remove the piece.
    """
    def capture(self, x, y):
        if not self.isFriendly(x, y):
            self.board.board[y][x] = None
        else:
            print("Invalid move! Friendly piece exists at coordinate specified.")

    """
        @desc: isFriendly returns a boolean indicating if a piece is on the same team.
        @param x: The x coordinate of the piece to check.
        @param y: The y coordinate of the piece to check.
        @return boolean: True if this piece is on the same piece as the the piece on (x,y).
    """
    def isFriendly(self, x, y):
        return True if self.board.board[y][x].color == self.color else False

    """
        @desc: isEmpty returns a boolean indicating if a empty position exists on the board.
        @param x: The X coordinate on the board to check.
        @param y: The Y coordinate on the board to check.
    """
    def isEmpty(self, x, y):
        return True if self.board.board[y][x] == None else False
        
    """
        @desc: Store move made into the Board lastMove attribute. Stores Color, Name, Old X position, Old Y position, New x Position, New y Position.
        storeMove(x, y):
        @param x: The new X coordinate the piece is being moved to.
        @param y: The new Y coordinate the piece is being moved to.
    """
    def storeMove(self, x, y):
        self.board.lastMove = self.color + self.name + str(self.x) + str(self.y) + str(x) + str(y)

    """
        @desc: isWithinBounds checks if given coordinate is within the board's boundaries.
        @param x: The X coordinate to check.
        @param y: The Y coordinate to check.
        @return boolean: True if within bounds, False otherwise.
    """
    def isWithinBounds(self, x, y):
        return True if x >= 0 and x < 8 and y >= 0 and y < 8  else False

    """
        @desc: isValidPath is an abstract method meant to check if all squares are valid up until destination coordinate.
        @param x: The final x coordinate the piece will arrive to.
        @param y: The final x coordinate the piece will arrive to.
    """
    def isValidPath(self, x, y):
        pass

    """
        @desc: isValidMove is a abstract method meant to returns a boolean indicating if a move is valid.
        @param x: The X coordinate the piece is requesting to move to.
        @param y: The Y coordinate the piece is requesting to move to.
        @return boolean: True if move can be made, False otherwise.
    """
    def isValidMove(self, x, y):
        pass

    """
        @desc: move is an abstract method meant to move a piece to given coordinate in the format: (x, y)
        @param x: The new X coordinate of the piece. (1 on Left, 8 on Right)
        @param y: The new Y coordinate of the piece. (A on Top, H on Bottom)
    """
    def move(self, x, y):
        pass
    
    """
        @desc: __str__ returns a string representation of the piece.
    """
    def __str__(self):
        return self.name

    """
        @desc: __repr__ returns a string representation of the piece.
    """
    def __repr__(self):
        return self.name