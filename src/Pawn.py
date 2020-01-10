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
    
    def validateMove(self, x: int, y: int) -> bool:
        pass

    def getPossibleMoves(self) -> List[List[int]]:
        pass