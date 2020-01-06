class Piece:

    def __init__(self, name, color, x, y, board):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.board = board
        self.moves = []

    def move(self, x, y):
        pass

    # Helper method.
    def capture(self, x, y):
        pass

    # Helper method.
    def isValidMove(self, x, y):
        pass

'''
    Methods:

        Move(x,y):
            1. Can only move 1 unit in the y direction after the initial move.
            2. The initial action can consist of moving 2 units in the y direction.
            3. The Pawn can use an 'en passent' which initially allows it to move
                1 unit in the x direction and 1 unit in the y direction if the enemy pawn
                attempts to save itself by moving 2 units in the y direction using it's 
                initial action.
            4. The pawn can capture other pieces diagonally (1 unit in the positive x and y direction).
'''
class Pawn(Piece):

    def __init__(self, name, color, x, y, board):
        super().__init__(name, color, x, y, board)

    

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