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

    # Evaluation only.
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

        return bestMove

    def minimaxRoot(self, depth, isMaximizingPlayer):

        moves = board.getAllPossibleMoves(self.team)
        bestMove = -9999
        bestMoveFound = random.choice(moves)
        boardCopy = board.getDeepCopy()

        for move in moves:
            boardCopy.update(move)
            value = self.minimax(depth - 1, boardCopy, -10000, 10000, not isMaximizingPlayer)

            if value >= bestMove:
                bestMove = value
                bestMoveFound = move
        
        return bestMoveFound

    def minimax(self, depth, board, alpha, beta, isMaximizingPlayer):
        
        if depth == 0:
            return -self.board.getEvaluation()
        
        moves = board.getAllPossibleMoves(self.team)

        if(isMaximizingPlayer):
            bestMove = -9999

            for move in moves:
                bestMove = max(bestMove, self.minimax(depth - 1, board, alpha, beta, not isMaximizingPlayer))
                alpha = max(alpha, bestMove)

                if beta <= alpha:
                    return bestMove
        else:
            bestMove = 9999
            
            for move in moves:
                bestMove = max(bestMove, self.minimax(depth - 1, board, alpha, beta, not isMaximizingPlayer))
                beta = min(beta, bestMove)
                
                if beta <= alpha:
                    return bestMove
        
        return bestMove

    def updateWorth(self):
        # Get value of all pieces.
        # Get value of all positions.
        # worth = value of all pieces + value of postions the pieces are on.
        pass

    def movePiece(self, move: str):
        self.board.update(move)


# TESTING
board = Board()
board.fillBoard()
player = Player(board, "B", False)
player.movePiece(player.minimaxRoot(2, False))

board.printBoard()
###
