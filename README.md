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

Structure:

    Piece
        King
        Queen
        Bishop
        Rook
        Knight
        Pawn
    Board

Additional Rules:

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

    Threefold Repetition:
        1. Requires a position to be repeated three times. Not moves. Castles, En Passent resets the possibility. A draw request may be made.

Piece Class:

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
        
        @desc: Returns a boolean indicating if a move is valid for any instance of the Piece class.
        isValidMove(x,y):
            @param X: The X coordinate the piece is requesting to move to.
            @param Y: The Y coordinate the piece is requesting to move to.
            @return boolean: True if move can be made, False otherwise.
        
        @desc: Checks if all squares are valid up until destination coordinate.
        isValidPath(x,y):
            @param X: The final X coordinate the piece will arrive to.
            @param Y: The final Y coordinate the piece will arrive to.
        
        @desc: Store move made into the Board lastMove attribute. Stores Color, Name, Old X position, Old Y position, New X Position, New Y Position.
        storeMove(x, y):
            @param X: The new X coordinate the piece is being moved to.
            @param Y: The new Y coordinate the piece is being moved to.

        @desc: Returns the difference in values. 
        difference(a, b):
            @param a: The starting value.
            @param b: The ending value.
            @return int: The absolute difference between two integers.

        @desc: Returns a boolean indicating if a piece is on the same team.
        isFriendly(x, y):
            @param X: The X coordinate of the piece to check.
            @param Y: The Y coordinate of the piece to check,.
            @return boolean: True if this piece is on the same piece as the the piece on (X,Y).
        
        @desc: Returns a boolean indicating if a empty position exists on the main board.
        isEmpty(x,y):
            @param X: The X coordinate on the board to check.
            @param Y: The Y coordinate on the board to check.

        @desc: Updates board with new position.
        update(x,y):
            @param X: The new X position of the piece.
            @param Y: The new Y position of the piece.

        