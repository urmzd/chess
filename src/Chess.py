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

    board.declareAsAI(aiTeam)

    chess = Chess(board, player1, player2, depth)

    #commands:
    # move - move 
    # help - gives a list of commands
    # draw - checks if 50 moves have been made.

    board.printBoard()
    
    while True:

        command = input("Type a command (type 'help' for a list of possible commands.): ")

        while command not in ["draw", "help", "move"]:
            command = input("Type a command (type 'help' for a list of possible commands.): ")

        if command == "draw":

            if board.canDeclareDraw() == True:
                print("The game has ended in a draw.")
                break
            else:
                print("The game not be declared as a draw currently. Current count without a pawn move or capture: {}. Make a move.".format(board.counter))
        
        elif command == "help":
            print("The following are the list of commands: ")
            print("help: Provides a list of possible commands.")
            print("draw: Ends the game in a draw if 50 moves have been made without a pawn capture or move.")
            print("move: Allows user to make a move.")

        else:

            if board.isCheckmate("B"):
                print("The game has ended. {} has won.".format("White"))
                break
            
            if board.isCheckmate("W"):
                print("The game has ended. {} has won.".format("Black"))
                break
                
            if board.isStalemate("W") or board.isStalemate("B"):
                print("The has ended in a draw.")
                break

            if startingPlayer.isAI == True:
                print ("----- AI MOVE -----")
                startingPlayer.move(startingPlayer.getBestMove(depth, True))
                board.printBoard()

                move = input("Type in a move in the format x1y1x2y2 (ex: e2e4): ")

                while move not in otherPlayer.getAllPossibleMoves():
                    print("{} is an invalid move. Try again.")
                    move = input("Type in a move in the format x1y1x2y2 (ex: e2e4): ")

                otherPlayer.move(move)

            else:
                startingPlayer.move(move)
                board.printBoard()
                
                move = input("Type in a move in the format x1y1x2y2 (ex: e2e4): ")
                while move not in startingPlayer.getAllPossibleMoves():
                    print("{} is an invalid move. Try again.")
                    move = input("Type in a move in the format x1y1x2y2 (ex: e2e4): ")

                print ("----- AI MOVE -----")
                otherPlayer.move(otherPlayer.getBestMove(depth, False))

            board.printBoard()