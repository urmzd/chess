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
        if self.team == "W":
            team = "B"
        else:
            team = "W"
        
        moves = self.board.getAllPossibleMoves(team)
        king = self.board.getKing(self.team)

        x = self.board.convertNumber(king.x)
        y = king.y + 1

        for move in moves:
            if move[2] == x and move[3] == str(y):
                return True
            else
                return False

    def isCheckmate(self):
        
        if self.board.getKing(self.team)

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

        if isMaximizingPlayer:
            bestMove = 9999
            team = "W"
        else:
            bestMove = -9999
            team = "B"

        boardCopy = board.getDeepCopy() # Get a copy of the main board.
        moves = boardCopy.getAllPossibleMoves(team) # Get all the possible moves.
        bestMoveFound = random.choice(moves) # Pick a random move.

        for move in moves:
            boardCopy = board.getDeepCopy()
            boardCopy.update(move)
            value = self.minimax(depth - 1, boardCopy, -10000, 10000, not isMaximizingPlayer)

            if value >= bestMove:
                bestMove = value
                bestMoveFound = move
        
        return bestMoveFound

    def minimax(self, depth, board, alpha, beta, isMaximizingPlayer):
        
        if depth == 0:
            return board.getEvaluation()

        if isMaximizingPlayer:
            team = "W"
        else:
            team = "B"
            
        moves = board.getAllPossibleMoves(team)

        if isMaximizingPlayer:
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

    def movePiece(self, move: str):
        self.board.update(move)

board = Board()
board.fillBoard()
player = Player(board, "W", False)
player.isCheck()