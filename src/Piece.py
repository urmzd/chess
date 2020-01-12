from typing import List

class Piece():

    """
        @desc: Super class all pieces will inherit their attributes from.

        @param team: Character representing name of team.
        @param name: Name of piece.
        @param icon: Unicode icon representing piece.
        @param value: Value of the piece.
        @param x: The current x position of piece.
        @param y: The current y position of piece.
        @param board: The Board instance the piece exists on.
        @param updated, Defaulted to False: Indicates whether set of possibleMoves have already been changed to match team.
    """
    def __init__(self, team: chr, name: chr, icon: chr, value: int, x: int, y: int, board: "Board", updated = False):
        self.team = team
        self.name = name
        self.icon = icon
        self.value = value
        self.x = x
        self.y = y
        self.board = board
        self.updated = updated
    
    """
        @desc: Moves piece on the board and removes any pieces that it lands on.
        @param x: The new x position of the piece.
        @param y: The new y position of the piece.
    """
    def move(self, x: int, y: int):
        self.storeMove(x,y) # Store move into Board instance's lastMove attribute.
        self.updated = True # Indicate that the possibleMove set has been used.

        if not self.board.isEmpty(x,y):
            self.capture(x, y) # Remove piece @ (x,y).
            self.board.resetCounter() # Reset 50-move rule counter since a capture has been made.

        self.incrementCounter() # Increase the number of moves made since the last capture / pawn move.
        self.board.board[y][x] = self # Move to location.
        self.board.board[self.y][self.x] = None # Remove old instance of self.
        self.x = x # Update x attribute.
        self.y = y # Update y attribute.

    """
        @desc: Removes piece at indicated location.
        @param x: The x location of the piece the user wishes to remove.
        @param y: The y location of the piece the user wishes to remove.
    """
    def capture(self, x: int, y: int):
        self.board.remove(x, y)
    
    """
        @desc: Checks if piece at indicated location is friendly or not.
        @param x: The x location of the piece to check.
        @param y: The y location of the piece to check.
        @return boolean: True if same team, False otherwise.
    """
    def isFriendly(self, x: int, y: int) -> bool:        
        return self.team == self.board.board[y][x].team

    """
        @desc: Checks if indicated location is a valid point on the board to move to.
        @param x: The x location to check.
        @param y: The y location to check.
        @return boolean: Returns true if point is contained within board, the position is empty or position contains enemy unit.
    """
    def validPosition(self, x: int, y: int) -> bool:
        if not self.board.contains(x,y):
            return False

        return self.board.isEmpty(x, y) or not self.isFriendly(x, y)
    
    """
        @desc: Get the proper move set for the current piece.
        @param moves: A list containing all the basic possible movements the piece can make.
        @return 2-D List: The inputted move list or the inverted version of the move list if the team is "B".
            Since the move list is defaulted for "W" / the white team.
    """
    def getMoveSet(self, moves: List[List[int]]) -> List[List[int]]:

        if self.team == "B":
            for moveset in range(len(moves)):
                for move in range(len(moves[moveset])):
                    moves[moveset][move] = -moves[moveset][move]

        return moves
    
    """
        @desc: Store a string of a move made in the lastMove attribute.
            Format: 'TeamName, Name, Current X, Current Y, New X, New Y'.
                Ex: 'BP0604'
        @param x: The x location the piece is moving to.
        @param y: The y location the piece is moving to.

    """
    def storeMove(self, x: int, y: int):
        self.board.lastMove = self.team + self.name + str(self.x) + str(self.y) + str(x) + str(y)
    
    """
        @desc: Returns a representation of the piece.
        @return: A copy of the icon representing the piece.
    """
    def __repr__(self):
        return self.icon

    """
        @desc: Abstract method that determines whether a move is valid or not.
        @param x: The desired x location.
        @param y: The desired y location.
        @param boolean: True if piece is allowed to move to position, False otherwise.
    """
    def validMove(self, x: int, int: int) -> bool:
        pass
    
    """
        @desc: Abstract method that updates the piece on the board if the move is deemed legal. Removing any enemy units if the piece will land on it.
        @param x: The new x location of the piece.
        @param y: The new y location of the piece.
        @return boolean: True if updated, False otherwise.
    """
    def update(self, x: int, y: int) -> bool:
        pass

    """
        @desc: Returns a List of all the possible moves the current piece can make. The following code is only for the King, Pawn and Knight.
            The Queen, Bishop and Rook will have their own implementation.
        @return 2-D List: A List of all the valid moves that can be made by the piece.
    """
    def getAllPossibleMoves(self) -> List[List[int]]:

        possibleMoves = self.getMoveSet(self.possibleMoves, self.team)
        validMoves = []

        for move in self.possibleMoves:
            if self.validMove(move[0], move[1]):
                validMoves.append(move)
            
        return validMoves