# Chess --> https://repl.it/repls/YellowishStingyConference
Chess game in Python Command Line. No GUI will implemented as of now.

The Chess Board will be labelled as following:

        A B C D E F G H
    1   R N B Q K B N R
    2   P P P P P P P P
    3
    4
    5
    6
    7   P P P P P P P P
    8   R N B Q K B N R

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

Notes:
    
    The X Coordinate will be converted from an ASCII character to an integer by the system.

    Legend:

        Name : {P, K, Q, R, K, B} : {Pawn, King, Queen, Rook, Knight, Bishop} : {1, 100, 9, 5, 3, 3 (Technically 3.5)}
        Color: {W, B} : {White, Black}


# NOTES

May add a possibleMoveSet to have easier implementation of A.I later on.

A.I will be a minimax algorithm with alpha-beta pruning.
Essentially, certain nodes will attempt to MAXIMIZE the "reward" while the minimizer will do the exact opposite
and attempt to minimize the reward. The algorithm is based on the idea that the participants will choose the most logic choice.

Alpha-beta pruning is a way of optimizing the algorithm. At it's core, it evaluates all nodes until it comes across a value which will not effect the end result.

For more information, watch/use theses:

1. https://youtu.be/zp3VMe0Jpf8 
2. https://www.youtube.com/watch?v=l-hh51ncgDI
3. https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/


# HOW TO RUN:

1. Access source folder.
2. Put the follow command in your terminal: 'python Chess.py'
