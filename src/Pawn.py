from typing import List
from Piece import Piece

"""
    @desc:
        The Pawn class inherits attributes from it's parent class Piece.
        Aditionally, it contains two of it's own attributes:

            1. played, which is set to False by default. This attribute is used to determine if the pawn can move 2 units.
            Note that, this attribute is set to True after its initial move, stopping it from moving 2 units from that point onwards.
            2. promoted, which is set to False by default. This attribute is used to determine if restrictions should be removed
            on the pawn. If the pawn is able to reach the end(s) of the board, the console will ask which "Piece" should the pawn 
            upgrade to. Upon confirmation, the promoted attribute is set to True and restrictions on the pawn are removed, allowing
            it to inherit move sets of other pieces.
            3. enPassent, which is set to False by default. On an valid attempt to use the En Passent move, the attribute will be set to
            true, allowing for other methods to use this information to remove the appropriate enemy pawn.
        
        Additional Notes:
            An En Passent can be used, which essentially allows the Pawn to capture the piece to it's side 
            by moving to the opposing pawn's x square and 1 unit behind the enemy pawn (like how it would attack a regular piece).
            However, this can only be used if the following condition are met:

                1. The last move made was the opposing enemy's pawn moved 2 squares towards the current pawn to prevent capture.
"""

class Pawn(Piece):

    def __init__(self, team, x, y, board):
        super().__init__("P", team, 1, x, y, board)
        self.played = False
        self.promoted  = False
        self.enPassent = False

    # @Override move

    def update(self, x: int, y: int):
        
        if self.validMove(x, y):
            if not self.board.isEmpty(x, y):
                if not self.board.isFriendly(x, y, self.team):
                    self.board.board[self.y][self.x].capture(x, y)

            if self.enPassent:
                if self.team == "W":
                    self.board.board[self.y][self.x].capture(x, y - 1)
                else:
                    self.board.board[self.y][self.x].capture(x, y + 1)
                
                self.enPassent = False # Reset so move cant be used again.

            self.played = True
            self.move(x, y)
        else:
            print("Invalid move.")

    # Determine if pawn is moving in the right direction.
    def validDirection(self, y: int) -> bool:
        
        if self.team == "W":
            if y > self.y:
                return True
        elif self.team == "B":
            if y < self.y:
                return True
        else:
            return False
        
    
    # Default returns false, unless the rules stated belowed are obliged, then it returns true.
    def validMove(self, x: int, y: int) -> bool:

        isValid = False # Default return value will be false.
        
        # 2 units forward for first move if not played.
        # 1 unit forward after that.
        # 1 unit left/right + 1 unit forward for attacks.
        # 1 unit left/right + 1 unit forward for en passent.
        # CANNOT GO BACKWARDS

        # For normal movement, not promoted
        if not self.played:

            if self.validDirection(y) and abs(y - self.y) == 2 and abs(x - self.x) == 0:
                for step in range(1, abs(y - self.y) + 1):
                    if self.team == "B":
                        step = -step

                    if not self.board.isEmpty(x, self.y + step):
                        return False
                isValid = True
        
        if self.validDirection(y) and abs(y - self.y) == 1 and abs(x - self.x) == 0:
            isValid = True
        
        attemptingToAttack = abs(y - self.y) == 1 and abs(x - self.x) == 1

        # For regular attack.
        if not self.board.isEmpty(x, y) and self.validDirection(y):
            if not isFriendly(x, y, self.team):
                if attemptingToAttack:
                    isValid = True
        
        # For En passent.
        # check attempting to attack            
        # BP1614
        # last move must have been made by a pawn, making 2 steps on left side or right
        # side of current pawn, 

        if self.board.isEmpty(x,y) and self.validDirection(y):
            if attemptingToAttack:
                lastMove = self.board.lastMove
                if lastMove[1] == "P" and lastMove[0] != self.team:
                    if int(lastMove[2]) - 1 == self.x or int(lastMove[2]) + 1 == self.x:
                        if abs(int(lastMove[3]) - int(lastMove[5])) == 2:
                            self.enPassent = True
                            isValid = True

        return isValid


    def getPossibleMoves(self) -> List[List[int]]:
        pass