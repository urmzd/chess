from Piece import Piece
from Pawn import Pawn
from King import King
from Knight import Knight
from Queen import Queen
from Rook import Rook
from Bishop import Bishop


class Board():

    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]
        self.counter = 0
        self.lastMove = ""

    def fillBoard(self):

        startingPositions = [1, 6]
        teams = ["W", "B"]

        for index in range(2):
            for x in range(8):
                self.board[startingPositions[index]][x] = Pawn(
                    teams[index], x, startingPositions[index], self)

        startingPositions = [0, 7]

        for index in range(2):
            self.board[startingPositions[index]][0] = Rook(
                teams[index], 0, startingPositions[index], self)
            self.board[startingPositions[index]][1] = Knight(
                teams[index], 1, startingPositions[index], self)
            self.board[startingPositions[index]][2] = Bishop(
                teams[index], 2, startingPositions[index], self)
            self.board[startingPositions[index]][3] = Queen(
                teams[index], 3, startingPositions[index], self)
            self.board[startingPositions[index]][4] = King(
                teams[index], 4, startingPositions[index], self)
            self.board[startingPositions[index]][5] = Bishop(
                teams[index], 5, startingPositions[index], self)
            self.board[startingPositions[index]][6] = Knight(
                teams[index], 6, startingPositions[index], self)
            self.board[startingPositions[index]][7] = Rook(
                teams[index], 7, startingPositions[index], self)

    def printBoard(self):

        print("  " + "A B C D E F G H" + "\n")
        line = ""

        for y in range(8):

            line = line + str(y + 1)

            for x in range(8):
                if self.board[y][x] == None:
                    line = line + " " + "-"
                else:
                    line = line + " " + repr(self.board[y][x])

            print(line + "  " + str(y + 1) + "\n")
            line = ""

        print("  " + "A B C D E F G H" + "\n")

    def remove(self, x: int, y: int):
        self.board[y][x] = None

    def isEmpty(self, x: int, y: int) -> bool:
        return self.board[y][x] == None

    def update(self, x: int, y: int, x1: int, y1: int):
        self.board[y][x].update(x1, y1)

    def update(self, move: str):
        self.board[int(move[1]) - 1][self.convertLetter(move[0])
                                     ].update(self.convertLetter(move[2]), int(move[3]) - 1)

    def convertLetter(self, letter: chr) -> int:
        return ord(letter) - 97

    def resetCounter(self):
        self.counter = 0

    def incrementCounter(self):
        self.counter += 1

    def contains(self, x: int, y: int):
        return x >= 0 and x < 8 and y >= 0 and y < 8


"""
###### TESTS 
board = Board()
board.fillBoard()
##### TEST GAME ####
board.update("e2e4")
board.update("e7e5")
board.update("f7f6")
board.update("g8e7")
board.update("g7g5")
board.update("f8h5")
board.update("e8g8") # Castle
board.update("b7b5")
board.update("b5b4")
board.update("a2a4")
board.update("b4a3") #en passent
board.update("a1a3")
board.update("d8e8")
board.update("e8f7")

board.printBoard()
##### TESTS
"""
