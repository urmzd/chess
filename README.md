# Chess
Chess game in Python Command Line. No GUI will implemented as of now.

The Chess Board will be labelled as following:

        1 2 3 4 5 6 7 8
    A   R N B Q K B N R
    B   P P P P P P P P
    C
    D
    E
    F
    G   P P P P P P P P
    H   R N B Q K B N R

Where Y(A ==> B) is the WHITE SIDE AND Y(G ==> H) is the BLACK SIDE

Structure:

    PIECE (SUPER)
        PAWN
        QUEEN
        KING
        BISHOP
        ROOK
        KNIGHT

SPECIAL CASES:

    En Passent:
        1. The opponents pawn has moved 2 units towards the friendly pawn to prevent itself from being captured.
        2. It must happen immediately after the pawn has moved or the friendly has forfeited the right to use the En Passent move.
    
    Castling:
        1. The king moves two steps towards any rook.
        2. The rook jumps over the king to the other side.
        3. King can not be in check.
        4. Rook and King may not have moved prior.

    Fifty Move Rule:
        1. A draw may be declared if a pawn hasn't been moved in the last 50 moves.
        2. OR a piece hasn't been captured in the last 50 moves.

    ## WILL IMPLEMENT THIS AFTER GAME IS COMPLETELY DONE
    Threefold Repetition:
        1. Requires a position to be repeated three times. NOT A MOVE(S). Castles, En Passent resets the possibility. A draw request may be made.

PIECE:

    Note:
        The Y Coordinate will be converted from an ASCII character to an integer by the system.

    Attributes:

        Name : {P, K, Q, R, K, B} : {Pawn, King, Queen, Rook, Knight, Bishop}
        Color: {W, B} : {White, Black}

    Methods:

        @desc: Moves piece to given coordinate in the format: (x, y)
        move(x,y):
            @param x: The new X coordinate of the piece. (1 on Left, 8 on Right)
            @param y: The new Y coordinate of the piece. (A on Top, H on Bottom)

        @desc: Removes piece at given coordinate in the format: (x,y)
        capture(x,y):
            @param x: The X coordinate in which to remove the piece. 
            @param y: The Y coordinate in which to remove the piece.

        @desc: Checks if given coordinate is within the board's boundaries.
        isWithinBounds(x,y):
            @param x: The X coordinate to check.
            @param y: The Y coordinate to check.
            @return boolean: True if within bounds, False otherwise.
        
        @desc: Checks if a move is valid for any instance of the Piece class.
        isValidMove(x,y):
            @param X: The X coordinate the piece is requesting to move to.
            @param Y: The Y coordinate the piece is requesting to move to.
            @return boolean: True if move can be made, False otherwise.
        
        @desc: Store move made into the Board lastMove attribute. Stores Color, Name, Old X position, Old Y position, New X Position, New Y Position.
        storeMove(x, y):
            @param X: The new X coordinate the piece is being moved to.
            @param Y: The new Y coordinate the piece is being moved to.

        