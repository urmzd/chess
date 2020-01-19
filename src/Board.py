from Utility import *
from typing import List
from Piece import Piece
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Rook import Rook

"""
    @desc: The Board class holds an array representing a board in the Chess game and the possible actions that can occur 
        on on the board such as the checkmate, stalemate, check.
"""
class Board():

    """
        @desc: Creates an instance of the class.
    """
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)] # A 8x8 grid holding all the pieces in the game.
        self.lastMove = "" # The last move made in the game.
        self.counter = 0 # The number of moves since the last pawn move or capture.

    """
        @desc: Checks if an empty spot exists at (x,y).
        @param x: The x location to check.
        @param y: The y location to check.
        @return Boolean: True if (x,y) is empty, False otherwise.
    """
    def isEmpty(self, x, y) -> bool:
        return self.board[y][x] == None

    """
        @desc: Check if a friendly piece exists at (x,y).
        @param x: The x location to check.
        @param y: The y location to check.
        @return Boolean: True if (x,y) is a friendly unit, False otherwise.
    """
    def isFriendly(self, x, y, team) -> bool:
        return self.board[y][x].team == team

    """
        @desc: Checks if a piece can be attacked at (x,y).
        @param x: The x location to check.
        @param y: The y location to check.
        @return Boolean: True if (x,y) is a non-empty enemy unit, False otherwise.
    """
    def canAttack(self, x, y, team) -> bool:
        return self.isEmpty(x, y) == False and self.isFriendly(x, y, team) == False

    """
        @desc: Checks if a point exists on the board.
        @param x: The x location to check.
        @param y: The y location to check.
        @return Boolean: True if (x,y) is greater than 0 and less than 8.
    """
    def contains(self, x, y) -> bool:
        return x >= 0 and x < 8 and y >= 0 and y < 8

    """
        @desc: Get all the possible moves a team can make.
        @param team: The team which is requesting a list of it's possible moves.
        @return List: A list of all the possible moves in string format.
    """
    def getAllPossibleMoves(self, team) -> List[str]:

        possibleMoves = []

        for row in self.board:
            for piece in row:
                if piece != None and piece.team == team:
                    piece.updatePossibleMoves()
                    possibleMoves += piece.possibleMoves

        return possibleMoves

    """
        @desc: Resets the counter attribute.
    """
    def resetCounter(self):
        self.counter = 0

    """
        @desc: Increments the counter attribute.
    """
    def incrementCounter(self):
        self.counter += 1

    """
        @desc: Fills the board with all the necessary pieces to play.
    """
    def fillBoard(self):
        startingPositions = [1, 6]
        teams = ["W", "B"]

        for index in range(2):
            for x in range(8):
                self.board[startingPositions[index]][x] = Pawn(
                    teams[index], self, x, startingPositions[index])

        startingPositions = [0, 7]

        for index in range(2):
            self.board[startingPositions[index]][0] = Rook(
                teams[index], self, 0, startingPositions[index])
            self.board[startingPositions[index]][1] = Knight(
                teams[index], self, 1, startingPositions[index])
            self.board[startingPositions[index]][2] = Bishop(
                teams[index], self, 2, startingPositions[index])
            self.board[startingPositions[index]][3] = Queen(
                teams[index], self, 3, startingPositions[index])
            self.board[startingPositions[index]][4] = King(
                teams[index], self, 4, startingPositions[index])
            self.board[startingPositions[index]][5] = Bishop(
                teams[index], self, 5, startingPositions[index])
            self.board[startingPositions[index]][6] = Knight(
                teams[index], self, 6, startingPositions[index])
            self.board[startingPositions[index]][7] = Rook(
                teams[index], self, 7, startingPositions[index])

    """
        @desc: Print the current state of the board.
    """
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

    """
        @desc: Declares all pawns on the specified team as an A.I.
        @param team: The team on which the pawns are an A.I.
    """
    def declareAsAI(self, team: chr):

        for row in self.board:
            for piece in row:
                if piece != None and piece.name == "p" and piece.team == team:
                    piece.isAI = True
    
    """
        @desc: Make a move on the board.
        @param move: A move in the string format indicating the starting and ending positions.
        @return Boolean: True if the move was made, False otherwise.
    """
    def makeMove(self, move: str) -> bool:
        
        intMoves = Utility.convertStringMoveToInt(move)
        xToCall = intMoves[0]
        yToCall = intMoves[1]

        if self.board[yToCall][xToCall] != None:
            self.board[yToCall][xToCall].updatePossibleMoves()
        else:
            print("{} is a illegal move. No piece exists at ({},{}) Try again.".format(move, xToCall, yToCall))
            return False

        if move in self.board[yToCall][xToCall].possibleMoves:
            self.board[yToCall][xToCall].move(move)
            return True
        else:
            print("{} is a illegal move. It's not a possible move. Try again.".format(move))
            return False

    """ 
        @desc: Add a piece on the board.
        @param piece: The piece to add onto the board.
        @param x: The x location to add it to.
        @param y: The y location to add it to.
    """
    def addPiece(self, piece: Piece, x: int, y: int):
        self.board[y][x] = piece

    """
        @desc: Remove a piece on the board.
        @param x: The x location to remove it from.
        @param y: The y location to remove it from.
    """
    def removePiece(self, x: int, y: int):
        self.board[y][x] = None

    """
        @desc: Gets an evaluation of the board.
        @return Integer: Returns the evaluation of the board based on each piece value and the positions they are located at.
    """
    def getEvaluation(self) -> int:

        evaluation = 0

        for row in self.board:
            for piece in row:
                if piece != None:
                    evaluation += (piece.value + Utility.getPositionEvaluation(piece.team, piece.name, piece.x, piece.y))
        
        return evaluation

    """
        @desc: Determines if the 50-move rule has occurred.
        @return Boolean: True if the move has occurred, False otherwise.
    """
    def canDeclareDraw(self) -> bool:

        if self.counter >= 50:
            return True
        else:
            return False
    
    """
        @desc: Gets the king from the specified team.
        @param team: The team which the king should be retrieved from.
        @return King: A king object with the specified team.
    """
    def getKing(self, team: chr):
        
        for row in self.board:
            for piece in row:
                if piece != None and type(piece) == King and piece.team == team:
                    return piece
        
        return None

    """
        @desc: Determines if a team is in checkmate.
        @param team: The team to check if a checkmate exists.
        @return Boolean: True if a team is in checkmate, False otherwise.
    """
    def isCheckmate(self, team: chr) -> bool:
        
        for move in self.getAllPossibleMoves(team):
            boardCopy = self.getDeepCopy()
            boardCopy.makeMove(move)

            if boardCopy.isCheck(team) == False:
                return False

        return True

    """
        @desc: Determines if a team is in check.
        @param team: The team to check if a check exists.
        @return Boolean: True if a team is in check, False otherwise.
    """
    def isCheck(self, team: chr) -> bool:

        king = self.getKing(team)
        kingX = Utility.convertToLetter(king.x)
        kingY = king.y
        
        if team == "W":
            possibleMoves = self.getAllPossibleMoves("B")
        else:
            possibleMoves = self.getAllPossibleMoves("W")

        for move in possibleMoves:
            
            if move[2] == kingX and int(move[3]) - 1 == kingY:
                return True

        return False

    """
        @desc: Determines a stalemate has occurred.
        @param team: The team which to check the stalemate has occurred with.
        @return Boolean: True if stalemate has occurred, False otherwise. 
    """
    def isStalemate(self, team: chr) -> bool:
        
        if self.isCheckmate(team) == False:

            for move in self.getAllPossibleMoves(team):
                boardCopy = self.getDeepCopy()
                boardCopy.makeMove(move)

                if boardCopy.isCheck(team) == False:
                    return False
            
            return True

        return False
    
    """ 
        @desc: Gets a deep copy of the current instance of the board.
        @return Board: Returns an instance of the current board.
    """
    def getDeepCopy(self):
        return copy.deepcopy(self)

    """
        @desc: Promotes a pawn to a different piece at the specified location.
        @param x: The x location of the pawn.
        @param y: The y location of the pawn.
        @param team: The team of the pawn.
        @param name: The name of the piece to promote it to.
    """
    def promotePawn(self, x: int, y: int, team: chr, name: chr):

        if name == "q":
            piece = Queen(team, self, x, y)
        elif name == "b":
            piece = Bishop(team, self, x, y)
        elif name == "n":
            piece = Knight(team, self, x, y)
        else:
            piece = Rook(team, self, x, y)
        
        self.removePiece(x, y) # Remove the pawn.
        self.addPiece(piece, x, y) # Add the new piece to the board.