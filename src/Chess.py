from Board import Board
from Player import Player
class Chess:

    def __init__(self, board, player1, player2, depth):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.depth = depth

        if player1.team == "W":
            self.maximizingPlayer = player1
        else:
            self.maximizingPlayer = player2

    
if __name__ == "__main__":
    
    depth = int(input("What depth would like the AI to reach? Type an integer: "))
    team = input("What team would like be on? Type 'W' for white and 'B' for black: ")

    if team == "W":
        aiTeam = "B"
    else:
        aiTeam = "W"
    
    board = Board()
    board.fillBoard()

    player1 = Player(team, board, False)
    player2 = Player(aiTeam, board, True)

    if team == "W":
        startingPlayer = player1
        otherPlayer = player2
    else:
        startingPlayer = player2
        otherPlayer = player1

    chess = Chess(board, player1, player2, depth)

    while True:

        if startingPlayer.isAI == True:
            startingPlayer.move(startingPlayer.getBestMove(depth, True))
            otherPlayer.move(input("Type in a move in the format x1y1x2y2 (ex: e2e4): "))
        else:
            startingPlayer.move(input("Type in a move in the format x1y1x2y2 (ex: e2e4): "))
            otherPlayer.move(otherPlayer.getBestMove(depth, False))

        board.printBoard()
