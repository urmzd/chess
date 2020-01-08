import Piece

'''
    Methods:

        Move(x,y):
            1. Can only move 1 unit in the y direction after the initial move.
            2. The initial action can consist of moving 2 units in the y direction.
            3. The Pawn can use an 'en passent' which initially allows it to move
                1 unit in the x direction and 1 unit in the y direction if the enemy pawn
                attempts to save itself by moving 2 units in the y direction using it's 
                initial action. This move can only be made immediately after the enemy makes a two step move.
                Otherwise, this right is lost.
            4. The pawn can capture other pieces diagonally (1 unit in the positive x and y direction).
'''
class Pawn(Piece):

    def __init__(self, name, color, x, y, board, played):
        super().__init__(name, color, x, y, board, False)

    ## Determines if pawn piece is only going forward/ backward (Depending on colour).
    def isCorrectDirection(self, y):
        
        if self.color == 'W':
            if y > self.y:
                return True
        else:
            if y < self.y:
                return True
        
        return False
    
    ## Checks if opposing pawn moved two steps on left or right side.
    def allowedEnPassent(self):

        # Ex: WPb2d2, BPg2e2
        # Check Colour: W (B), B (G)
        # Convert B to 2
        # Convert D to 4
        # Convert G to 7
        # Convert E to 5
        # Subtract abs(D - B) = 2 (En Passent Allowed) for Any Pawn on (1, D) or (3, D)
        # Subtract abs(G - E) = 2 (En Passent Allowed) for Any Pawn on (1, E) or (3, E)
        lastMove = self.board.lastMove

        if lastMove[1] == "P":
            if int(lastMove[3]) - 1 == self.x or int(lastMove[3]) + 1 == self.x:
                if lastMove[0] == "B":
                    if lastMove[2] == "g":
                        if lastMove[4] == "e":
                            return True
                else:
                    if lastMove[2] == "b":
                        if lastMove[4] == "d":
                            return True
        return False


    # if not played, can move 2 spots in the y direction.
    # if moved only spot is allowed.
    # only diagonal attacks are allowed. Check if enemy exists on (1,1) on either side.
    # An "en passent" can be made if the opponent moves two units to prevent being captured AND
    ## NO OTHER MOVE HAS BEEN MADE SINCE THEN.
    def isValidMove(self, x, y):
        
        # If move will result in out of bounds or is in wrong direction, return false.
        if not self.isCorrectDirection(y) or not self.isWithinBounds(x,y):
            return False
        
        # If the pawn hasn't moved yet, it can move 2 moves.
        if not self.played and self.difference(x, self.x) == 0:
            if self.difference(y, self.y) == 2:
                return True

        # If attempting to En Passent, ensure that it's doing it right.
        if self.allowedEnPassent() and self.difference(x, self.x) == 1 and difference(y, self.y) == 1 and x == int(self.board.lastMove[3]):
            return True

        # If a capture can be made, Then its a valid move.
        if not self.isEmpty(x,y) and self.difference(x, self.x) == 1 and self.difference(y, self.y) == 1 and not self.isFriendly(x,y):
            return True

        # If the pawn is moving one step and no obstacles are around it, it's a valid move.
        if self.difference(x, self.x) == 1 and self.difference(y, self.y) == 0 and self.isEmpty(x,y):
            return True

        return False

    def move(self, x,y):
        
        if self.isValidMove(x,y):
            self.storeMove(x, y) # Store move.
                if self.allowedEnPassent(x, y):
                    if self.color == "W":
                        self.capture(x, y - 1) #remove enemy behind
                    else:
                        self.capture(x, y + 1) #remove enemy 'ahead'
                else:
                    self.capture(x, y) # Remove enemy.
    
            self.x = x #update board
            self.y = y #update board
