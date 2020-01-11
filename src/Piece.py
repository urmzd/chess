from typing import List

"""
    @desc:
        The Piece class is a class that is meant to parent other classes such as:

            Pawn,
            King,
            Queen,
            Bishop,
            Knight,
            Rook.
        
        It contains four abstract methods that all children must inherit, these are:

            1. isValidPath(x, y), which validates all units up until the destination.
            2. isValidMove(x, y), which validates the unit chosen.
            3. getPossibleValues(), which returns an array filled will all possible moves in the form [x,y].
            4. move(x, y), which moves the piece to postion (x, y) and removes any opposing piece if it lands on it.

"""
class Piece:

    """
        @desc: Constructs an instance of the Piece class.
        @param name: A string representing the name of the piece.
        @param team: A string representing the team of the piece.
        @param value: An integer representing the 'value' of the piece.
        @param x: The x position of the piece on the game board.
        @param y: The y position of the piece on the game board.
        @param board: An instance of the Board class on which the piece will be interacted with.
    """
    def __init__(self, name: str, team: str, value: int, x: int, y: int, board):
        self.name = name
        self.team = team
        self.value = value
        self.x = x
        self.y = y
        self.board = board

    """
        @desc: Removes a piece on the board.
        @param x: The x position of the piece to remove.
        @param y: The y position of the piece to remove.
    """
    def capture(self, x: int, y: int):
        self.board.board[y][x] = None # Clears piece at position.

    """
        @desc: Stores a string into the Board instance in the form: "TN(x1,y1)(x2,y2)".
        @param x: The new x position of the piece that will be moving.
        @param y: The new y position of the piece that will be moving.
    """
    def storeMove(self, x: int, y: int):
        self.board.lastMove = self.team + self.name + str(self.x) + str(self.y) + str(x) + str(y)

    """
        @desc: Checks if a position (x,y) is valid by determining if it is within the borders of the board.
        @param x: The requested x position to check.
        @param y: The requested y position to check.
        @return boolean: True if x and y are in the range of 8.
    """
    def isWithinBoard(self, x: int, y: int) -> bool:
        return x >= 0 and x < 8 and y >= 0 and y < 8

    """
        @desc: Checks if unit is allowed at position (x,y).
        @param x: The x position to check.
        @param y: The y position to check.
        @return boolean: True if all units are empty, False otherwise.
    """
    def validMove(self, x: int, y: int) -> bool:
        pass
    
    """
        @desc: Determines all the possible moves a piece can be make.
        @return: A list containing x and y positions in the form [x,y].
    """
    def getPossibleMoves(self) -> List[List[int]]:
        pass

    """
        @desc: Updates the position (x,y) of the piece on the board.
        @param x: The new x position of the piece.
        @param y: The new y position of the piece.
    """
    def move(self, x: int, y: int):
        pass

    # String representation.
    def __repr__(self):
        return self.name