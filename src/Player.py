from Board import Board

class Player():

    def __init__(self, team: chr, board, isAI):
        self.team = team
        self.board = board
        self.isAI = isAI

    def move(self, move: str):

        self.board.makeMove(move)

    def getBestMove(self, depth, isMaximizingPlayer):

        if isMaximizingPlayer:
            bestMove = 9999
            team = "W"
        else:
            bestMove = -9999
            team = "B"

        moves = self.board.getAllPossibleMoves(team)
        bestMoveFound = ""

        for move in moves:
            boardCopy = self.board.getDeepCopy()
            boardCopy.makeMove(move)
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