# Chess

#Preface
        The Chess game will be a command-line based version of the popular board game 'Chess'
        
The Chess Board will be labelled as following (icons will replace the letters in the actual game):

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
    Player
    Chess
    Utility

# NOTES

The A.I will be consist of the minimax algorithm with alpha-beta pruning.
Essentially, certain nodes will attempt to maximize the "reward" while the minimizer will do the exact opposite
and attempt to minimize the "reward". The reward in this case being, the board evaluation.  The algorithm is based on the idea that the participants will choose the most logic choice.

Alpha-beta pruning is a way of optimizing the algorithm. At it's core, it evaluates all nodes until it comes across a value which will not effect the end result.

For more information, watch/use theses:

1. https://youtu.be/zp3VMe0Jpf8 
2. https://www.youtube.com/watch?v=l-hh51ncgDI
3. https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/


# HOW TO RUN:

1. First, ensure that you have Python 3.7 + installed.
2. Access source folder.
3. Put the follow command in your terminal: 'python Chess.py'
4. Have fun playing! Type 'help' in the terminal for assistance in learning more about the game.

# TODO:

1. Add comments to source files to ensure code is maintainable later down the line.
