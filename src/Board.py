from Utility import *
from typing import List
from Piece import Piece
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Rook import Rook


class Board():

    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]
        self.lastMove = ""
        self.counter = 0

    def isEmpty(self, x, y) -> bool:
        return self.board[y][x] == None

    def isFriendly(self, x, y, team) -> bool:
        return self.board[y][x].team == team

    def canAttack(self, x, y, team) -> bool:
        return self.isEmpty(x, y) == False and self.isFriendly(x, y, team) == False

    def contains(self, x, y) -> bool:
        return x >= 0 and x < 8 and y >= 0 and y < 8

    def getAllPossibleMoves(self, team) -> List[str]:

        possibleMoves = []

        for row in self.board:
            for piece in row:
                if piece != None and piece.team == team:
                    piece.updatePossibleMoves()
                    possibleMoves += piece.possibleMoves

        return possibleMoves

    def resetCounter(self):
        self.counter = 0

    def incrementCounter(self):
        self.counter += 1

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

    def declareAsAI(self, team: chr):

        for row in self.board:
            for piece in row:
                if piece != None and piece.name == "p" and piece.team == team:
                    piece.isAI = True
    
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

    def addPiece(self, piece: Piece, x: int, y: int):
        self.board[y][x] = piece

    def removePiece(self, x: int, y: int):
        self.board[y][x] = None

    def getEvaluation(self) -> int:

        evaluation = 0

        for row in self.board:
            for piece in row:
                if piece != None:
                    evaluation += (piece.value + Utility.getPositionEvaluation(piece.team, piece.name, piece.x, piece.y))
        
        return evaluation

    def canDeclareDraw(self) -> bool: # 50 move rule.

        if self.counter >= 50:
            return True
        else:
            return False
    
    def getKing(self, team: chr):
        
        for row in self.board:
            for piece in row:
                if piece != None and type(piece) == King and piece.team == team:
                    return piece

    def isCheckmate(self, team: chr) -> bool:
        
        for move in self.getAllPossibleMoves(team):
            boardCopy = self.getDeepCopy()
            boardCopy.makeMove(move)

            if boardCopy.isCheck(team) == False:
                return False

        return True

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

    def isStalemate(self, team: chr) -> bool:
        
        if self.isCheckmate(team) == False:

            for move in self.getAllPossibleMoves(team):
                boardCopy = self.getDeepCopy()
                boardCopy.makeMove(move)

                if boardCopy.isCheck(team) == False:
                    return False
            
            return True
        else:
            return False

    def getDeepCopy(self):
        return copy.deepcopy(self)

    def promotePawn(self, x: int, y: int, team: chr, name: chr):

        if name == "q":
            piece = Queen(team, self, x, y)
        elif name == "b":
            piece = Bishop(team, self, x, y)
        elif name == "n":
            piece = Knight(team, self, x, y)
        else:
            piece = Rook(team, self, x, y)
        
        self.removePiece(x, y)
        self.addPiece(piece, x, y)