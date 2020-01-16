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

    #commands:
    # move - move 
    # help - gives a list of commands
    # draw - checks if 50 moves have been made.

    """startingPlayer.move("e2e4")
    otherPlayer.move(otherPlayer.getBestMove(depth, False))
    startingPlayer.move("d2d4")
    otherPlayer.move(otherPlayer.getBestMove(depth, False))"""

    board.printBoard()
    
    while True:

        if startingPlayer.board.isCheckmate(startingPlayer.team):
            print("{} has won.".format(startingPlayer.team))
            break
        
        if otherPlayer.board.isCheckmate(otherPlayer.team):
            print("{} has won.".format(otherPlayer.team))
            break

        if startingPlayer.isAI == True:
            startingPlayer.move(startingPlayer.getBestMove(depth, True))

            move = input("Type in a move in the format x1y1x2y2 (ex: e2e4) or a command (help for more details): ")

            if otherPlayer.validateMove(move) == False:
                while True:
                    move = input("Type in a move in the format x1y1x2y2 (ex: e2e4) or a command (help for more details): ")
                    if otherPlayer.validateMove(move) == True:
                        break

            otherPlayer.move(move)

        else:
            move = input("Type in a move in the format x1y1x2y2 (ex: e2e4) or a command (help for more details): ")

            if startingPlayer.validateMove(move) == False:
                while True:
                    move = input("Type in a move in the format x1y1x2y2 (ex: e2e4) or a command (help for more details): ")
                    if startingPlayer.validateMove(move) == True:
                        break

            startingPlayer.move(move)

            otherPlayer.move(otherPlayer.getBestMove(depth, False))

        board.printBoard()
    
