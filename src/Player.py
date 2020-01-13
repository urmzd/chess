from Board import Board
from random import randrange

class Player:

    def __init__(self, board, team, isAI):
        self.board = board
        self.team = team
        self.isAI = isAI
        self.inCheck = False

    def isCheck(self):
        # Get position of King
        # Check if position of King is a valid move for all pieces on the current team
        # If it is, this player is inCheck
        pass

    def isCheckmate(self):
        pass

    def makeRandomMove(self):
        moves = board.getAllPossibleMoves(self.team)
        self.movePiece(moves[randrange(len(moves))])

    ## Generate temp board, make a move and evaluate the board. The score that minimizes opponents score.
    def calculateBestMove(self):

        pass

    def updateWorth(self):
        # Get value of all pieces.
        # Get value of all positions.
        # worth = value of all pieces + value of postions the pieces are on.
        pass

    def movePiece(self, move: str):
        self.board.update(move)

### TESTING
board = Board()
board.fillBoard()
player = Player(board, "W", False)
player.makeRandomMove()
board.printBoard()
###