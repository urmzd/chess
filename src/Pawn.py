import Piece

"""
    @desc: The Pawn class inherits some attributes from the its parent class, Piece.
    It also contains it's own attributes differentiating it from other pieces.
    The Pawn in Chess is allowed to move only 1 unit forward, unless it's on the first move,
    which then it is allowed move 2 units forward. If the Pawn can reach the end(s) of the board,
    it can be "promoted" to any piece (except to a King). It can only capture diagonally and only if
    there is a piece on the on the left or ride diagonals of the pawn. Except for when using the En Passent
    rule which allows it to capture the pawn behind it immediately after the opposing pawn has moved two
    moves towards the current pawn in order to avoid capture and there is no other piece on that unit.
    In case there is a unit already there, the pawn will only capture that piece and the other piece will not
    be captured. Also, the pawn can only move if all units it is moving towards are empty.
"""

"""
    @Todo: add new move-sets when the pawn is promoted.
"""
class Pawn(Piece):

    """
        @desc: The class constructor which creates a new Pawn piece.
        @param name: By default, a pawn will have the name "P" to indicate it is indeed a pawn.
        @param color: The team the pawn is on, "W" for white, "B" for black.
        @param x: The starting x position.
        @param y: The starting y position.
        @param played: A boolean which is set to False by default to indicate the piece has not moved.
        @param promoted: A boolean which is set to False by default to indicate the "Pawn" does not have 
            additional privileges.
    """
    def __init__(self, name, color, x, y, board, played, promoted):
        super().__init__("P", color, x, y, board, False, False)

    """
        @desc: isCorrectionDirection determines if the pawn piece is going in the right direction.
        @param y: The requested y location.
        @return boolean: True if correct direction, False otherwise.
    """
    def isCorrectDirection(self, y):
        
        """
            Since all white pawns start @ y = 2, in order for the y argument to be valid,
                the y argument must be greater than the pawn's current y value.

            The opposite is true for black pawns which start @ y = 7, therefore the y argument is only valid,
                the y argument must be less than the pawn's current y value.
        """
        if self.color == 'W':
            if y > self.y:
                return True
        else:
            if y < self.y:
                return True
        
        return False
    
    """
        @desc: allowedEnPassent determines if the pawn is allowed to use the En Passent move,
        which essentially allows it to go 1 unit to the left or right and 1 unit forward, in order to capture the pawn
        behind it.
        @param x: The x location the pawn is requesting to move to.
        @param y: The y location the pawn is requesting to move to.
        @return boolean: True if the pawn is allowed to use the En Passent move, False otherwise.
    """
    def allowedEnPassent(self, x, y):

        lastMove = self.board.lastMove # Get the last move, example move: WP1214.

        # The En Passent can only be used if the unit where the pawn is moving is empty.
        if not isEmpty(x, y):
            return False
        
        if lastMove[1] == "P": # Ensure that the last move was made by a pawn.
            # Ensure that the piece moved is either on the left or right side of the current pawn.
            if int(lastMove[2]) - 1 == self.x or int(lastMove[2]) + 1 == self.x:
                # Check what color pawn moved.
                if lastMove[0] == "B":
                    # If it was black, check that the opposing pawn moved 2 units towards current pawn.
                    if int(lastMove[3]) == 7:
                        if int(lastMove[5]) == 5:
                            return True
                else: # Otherwise, in case the pawn is white.
                    # Check that the opposing pawn moved 2 units towards current pawn.
                    if lastMove[3] == 2 :
                        if lastMove[5] == 4:
                            return True
        return False

    """
        @desc: isValidPath checks if the units the pawn is moving through are empty. In other words,
        it checks if each spot on the board has no friendly or opposing unit on it.
        @param x: The x location the pawn is requesting to move to.
        @param y: The y location the pawn is requesting to move to.
        @return boolean: True if the pawn can move to the final location, false otherwise.
    """
    def isValidPath(self, x, y):

        # Check that if 2 units are being moved, the spaces being moved is empty.
        for step in range(self.difference(y, self.y)):
            if not self.isEmpty(x, y + step):
                return False

        return True

    """
        @desc: isValidMove checks if the move being requested can be made.
        @param x: The x location the pawn is requesting to move to.
        @param y: The y location the pawn is requesting to move to.
        @return boolean: True if the pawn can make the move being requested, false otherwise.
    """
    def isValidMove(self, x, y):

        """A move is invalid if it is going in the wrong direction or will result in the piece going out
        of bounds."""
        if not self.isCorrectDirection(y) or not self.isWithinBounds(x,y):
            return False

        # If no x move is being made.
        if self.difference(x, self.x) == 0:
            # Check that the pawn hasn't moved already, the path is valid and 2 steps are being requested.
            if not self.played and self.isValidPath(x,y) and self.difference(y, self.y) == 2:
                return True # It is a valid request.
            # If the pawn is requesting to move 1 unit and the unit is empty.
            if self.isEmpty(x,y) and self.difference(y, self.y) == 1 and :
                return True # It is a valid request.

        # If a capture attempt is being made.
        if self.difference(x, self.x) == 1 and self.difference(y, self.y) == 1:
            
            """If an En Passent is allowed and the x location is on the same x location
            of the enemy pawn.
            """
            if self.allowedEnPassent(x, y) and x == int(self.board.lastMove[3]):
                return True # The request is valid.
            
            # If the unit is not empty and the unit contains an enemy.
            if not self.isEmpty(x,y) and not self.isFriendly(x,y):
                return True # The request is valid.
    

        return False

    """
        @desc: move determines if a valid request is being moved and updates the board accordingly.
        @param x: The x location the piece is requesting to move to.
        @param y: The y location the piece is requesting to move to.
    """
    def move(self, x, y):
        
        # Check if a valid move request is being made.
        if self.isValidMove(x,y):
            
            # Update played attribute to ensure that piece does not move 2 units after this move.
            if self.played == False:
                self.played = True

            self.storeMove(x, y) # Store move into lastMove board attribute.

            # Check if an En Passent is being requested.
            if self.allowedEnPassent(x, y):
                if self.color == "W": # If colour is white.
                    self.capture(x, y - 1) # Remove piece behind.
                else:
                    self.capture(x, y + 1) # Otherwise, remove piece ahead.
            else: # Otherwise, capture piece at requested location.
                self.capture(x, y) 

            self.update(x, y) # Update piece on board.
        else:
            # Print error incase an invalid move is being made.
            print("The move request is invalid. Try something else.")