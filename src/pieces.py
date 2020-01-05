class Piece:

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y


    def move(self, x, y):
        pass

class Pawn(Piece):

    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

class King(Piece):

    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

class Queen(Piece):

    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

class Knight(Piece):

    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

class Rook(Piece):

    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

class Bishop(Piece):

    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)