from Board import Board

"""
    @desc: The Player class represents a player in the game. 
        It contains methods to move a piece on the board, get the possible moves that can be made
        and methods that implement the minimax algorithm with alpha-beta pruning.
"""
class Player():

    """
        @desc: Creates an instance of the Player object.
        @param team: Team, 'W' for white team, 'B' for black team.
        @param board: The board in which the player is going to be active on.
        @param isAI: Indicates if player is A.I or not.
    """
    def __init__(self, team: chr, board, isAI):
        self.team = team
        self.board = board
        self.isAI = isAI

    """
        @desc: Manipulates pieces on the game board.
        @param move: A string consisting of the starting and ending location of the piece (ex: 'e2e4').
    """
    def move(self, move: str):

        self.board.makeMove(move)

    """
        @desc: Retrieves all the possible moves the current player can make.
        @return List: A list consisting of strings/moves the player can make.
    """
    def getAllPossibleMoves(self):

        return self.board.getAllPossibleMoves(self.team)

    """
        @desc: Helper method to assist in the retrieval of the best move.
        @param depth: The number of moves to look ahead to.
        @return String: The best possible move the current player can make.
    """
    def getBestMove(self, depth):
        if self.team == "W":
            team = True
        else:
            team = False

        return self.minimaxRoot(depth, team)

    """
        @desc: Gets the best possible move a player can make by evaluating future logical moves and basing its own evaluation off that.
        @param depth: The number of moves to look ahead to.
        @param isMaximizingPlayer: Indicates weather player is the one maximizing the board's value ('W') or is attempting to minimize it ('B').
        @return String: The best possible move the current player can make.
    """
    def minimaxRoot(self, depth, isMaximizingPlayer) -> str:

        # Check if player is attempting to maximize or minimize the board evaluation.
        if isMaximizingPlayer:
            bestMove = -9999 # Start with some arbitrary low number.
            team = "W" # Declare that the current team is 'W'/white.
        else:
            bestMove = 9999 # Start with some arbitrary high number.
            team = "B" # Declare that the current team is 'B'/black.

        # All the possible moves that can be made.
        moves = self.board.getAllPossibleMoves(team)
        bestMoveFound = "" # Holds the best possible move that can made.

        # Iterate through each possible move to find which optimizes the reward.
        for move in moves:
            boardCopy = self.board.getDeepCopy() # Get a copy of the board.
            boardCopy.makeMove(move) # Make the move.
            value = self.minimax(depth - 1, boardCopy, -10000, 10000, not isMaximizingPlayer) # Evaluate move made.

            # If new best move is found, store within the bestMoveFound variable.
            if team == "W" and value >= bestMove:
                bestMove = value
                bestMoveFound = move
            
            if team == "B" and value <= bestMove:
                bestMove = value
                bestMoveFound = move
        
        return bestMoveFound # Return the best move possible.

    """
        @desc: The minimax algorithm is a recursive algorithm which determines the best possible outcome,
            with the assumption that one agent will always attempt to maximize the reward and one agent will
            always attempt to minimize the reward.
        @param depth: The number of steps to look ahead.
        @param board: The board instance in which to check the possible moves.
        @param alpha: Holds the value of a node (attempts to maximize).
        @param beta: Holds the value of a node (attempts to minimize).
        @param isMaximizingPlayer: Indicates if player will attempt to maximize or minimize board evalation.
        @return Integer: Returns the best possible board evaluation.
    """
    def minimax(self, depth, board, alpha, beta, isMaximizingPlayer) -> int:
        
        # Return evaluation upon reaching leaf nodes.
        if depth == 0:
            return board.getEvaluation()
        
        # The maximizing player will always be the white team.
        if isMaximizingPlayer:
            team = "W"
            bestMove = -9999
        else:
            team = "B"
            bestMove = 9999

        # Get a list of all the possible moves.
        moves = board.getAllPossibleMoves(team)
        
        # Determine if player is attempting to maximize or minimize the board evaluation.
        if isMaximizingPlayer:
            # Iterate through each move.
            for move in moves:
                # Get the max value possible by comparing the current best move and the other possible moves.
                bestMove = max(bestMove, self.minimax(depth - 1, board, alpha, beta, not isMaximizingPlayer))
                alpha = max(alpha, bestMove)

                # If the the other outcomes can't affect the current best move, return the current evaluation.
                if beta <= alpha:
                    return bestMove
        else:            
            # Iterate through each move.
            for move in moves:
                # Get the min value possible by comparing the current best move and the other possible moves.
                bestMove = min(bestMove, self.minimax(depth - 1, board, alpha, beta, not isMaximizingPlayer))
                beta = min(beta, bestMove)
                
                # If the other outcomes can't affect the current best, return the current evaluation.
                if beta <= alpha:
                    return bestMove
        
        return bestMove # Return evaluation.