# chess
Chess game in Python


Structure:

    PIECE (SUPER)
        PAWN
        QUEEN
        KING
        BISHOP
        ROOK
        KNIGHT
    


    Castling: requires history of involved rook and king. Can be accomplished via a hasMovedBefore flag.
    en Passant: Knowledge of the last move taken. Can be accommodated by retaining a lastMove data structure, or retaining the previous board state.
    Fifty move rule: requires history of when the last capture or pawn move. Can be accomplished via a lastPawnMoveOrCapture counter
    Threefold repetition: requires all previous board states since the last castle, pawn move or capture. A list of hashes of previous states may be an option. (Thanks dfeuer)

@https://stackoverflow.com/questions/24686803/need-help-implementing-en-passant-pawn-capture-and-promotion
