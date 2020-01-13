from Board import Board
import random

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
        self.board.getKing(self.team)
        pass

    def isCheckmate(self):
        pass

    def getRandomMove(self):
        moves = board.getAllPossibleMoves(self.team)
        return random.choice(moves)

    ## Generate temp board, make a move and evaluate the board. The score that minimizes opponents score.
    def calculateBestMove(self) -> str:
        moves = board.getAllPossibleMoves(self.team)

        if self.team == "W":
            bestValue = 9999
        else:
            bestValue = -9999
            
        bestMove = self.getRandomMove()

        for move in moves:
            boardCopy = board.getDeepCopy()
            boardCopy.update(move)
            boardValue = board.getEvaluation()

            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move
        
        print(bestMove)
        return bestMove

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
player = Player(board, "B", False)
player.movePiece(player.calculateBestMove())
player.movePiece(player.calculateBestMove())
player.movePiece(player.calculateBestMove())

board.printBoard()
###