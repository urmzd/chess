from Piece import Piece
from Pawn import Pawn
from King import King
from Knight import Knight
from Queen import Queen
from Rook import Rook
from Bishop import Bishop

"""
    @desc: The Board class holds all the pieces in the game and contains methods to 
    update the position of the pieces and attributes to hold information for rules such
    as the 50-move rule and threefold-repetition rule.
"""
class Board:

    """
        @desc: A constructor which create a board for the chess pieces to move on.
    """
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)] # A 8 x 8 board.
        self.counter = 0 # Number of moves since the last capture or pawn move.
        self.lastMove = "" # A string to hold the last move made in string format.
    
    """
        @desc: Fills board will all the required pieces to play.
    """
    def fillBoard(self):
        
        for x in range(8):
            self.board[1][x] = Pawn("W", x, 1, self)
            self.board[6][x] = Pawn("B", x, 6, self)

        colors = ["W", "B"]
        yLocations = [0, 7]

        for i in range(2):
            self.board[yLocations[i]][0] = Rook(colors[i], 0, yLocations[i], self)
            #self.board[yLocations[i]][1] = Knight(colors[i], 1, yLocations[i], self)
            #self.board[yLocations[i]][2] = Bishop(colors[i], 2, yLocations[i], self)
            #self.board[yLocations[i]][3] = Queen(colors[i], 3, yLocations[i], self)
            self.board[yLocations[i]][4] = King(colors[i], 4, yLocations[i], self)
            #self.board[yLocations[i]][5] = Bishop(colors[i], 5, yLocations[i], self)
            #self.board[yLocations[i]][6] = Knight(colors[i], 6, yLocations[i], self)
            self.board[yLocations[i]][7] = Rook(colors[i], 7, yLocations[i], self)
            
    """
        @desc: move takes a piece at (x1, y2) and moves it to (x2, y2) as long as the move is valid.
        @param x1: The x location of the piece to be moved.
        @param y1: The y location of the piece to be moved.
        @param x2: The x location the piece is being requested to move to.
        @param y2: The y location the piece is being requested to move to.
    """
    def update(self, x1: int, y1: int, x2: int, y2: int):
        self.board[y1][x1].update(x2, y2)

    """
        @desc: convertAlpha converts lower case alphabets in the ASCII set to a integer.
        @param letter: The ASCII letter to convert.
        @param case: True for upper case letters, false for lower case letters.
    """
    def convertAlpha(self, letter: chr, case: bool) -> int:
        if case:
            return ord(chr(letter)) - 65
        else:
            return ord(chr(letter) - 97)

    """
        @desc: convertNumber converts number to alphabet form the ASCII set.
        @param number: The number to convert.
        @param case: True for upper case letters, false for lower case letters.
    """
    def convertNumber(self, number: int, case: bool) -> chr:
        if case:
            return chr(number + 65)
        else:
            return chr(number + 97)

    """
        @desc: Checks if a position (x,y) is valid by determining if it is within the borders of the board.
        @param x: The requested x position to check.
        @param y: The requested y position to check.
        @return boolean: True if x and y are in the range of 8.
    """
    def isWithinBoard(self, x: int, y: int) -> bool:
        return x >= 0 and x < 8 and y >= 0 and y < 8

    """
        @desc: Prints all pieces on the board.
    """
    def printBoard(self):

        line = "" # Line to print.
        topLine = "  A B C D E F G H"

        print(topLine + "\n")
        # Iterates through the board and prints each piece.
        for x in range(8):

            line = line + str(x + 1)

            for y in range(8):
                if self.board[x][y] == None:
                    line = line + " " + "-" # In case no piece exists at unit.
                else:
                    line = line + " " + repr(self.board[x][y])
            print(line + "\n") # New line for every 8 pieces printed.
            line = ""

    ## Check if (x,y) is empty.
    def isEmpty(self, x: int, y: int) -> bool:
        return self.board[y][x] == None
    
    # Checks if current team is the same as the piece on board[y][x].
    def isFriendly(self, x: int, y: int, team: str) -> bool:
        return  team == self.board[y][x].team
    
    def resetCounter(self):
        self.counter = 0


#TEST PAWN
board = Board()
board.fillBoard()
board.printBoard()

board.update(4, 7, 6, 7)
board.printBoard()