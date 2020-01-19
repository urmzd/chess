# Chess

# Preface
The 'chess' game is a command-line based version of the popular board game 'Chess'.
        
The Chess board will be labelled as following (icons will replace the letters in the actual game):

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
and attempt to minimize the "reward". The reward in this case being, the worth of the board.  The algorithm is based on the idea that the participants will choose the most logic choice.

Alpha-beta pruning is a way of optimizing the algorithm. At its core, it evaluates nodes until it reaches a point where the already evaluated.

For more information, feel free to use these:

1. https://youtu.be/zp3VMe0Jpf8 
2. https://www.youtube.com/watch?v=l-hh51ncgDI
3. https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/


# HOW TO RUN:

1. First, ensure that you have Python 3.8+ installed.
2. Access source folder.
3. Put the follow command in your terminal: 'python Chess.py'.
4. Have fun playing! Type 'help' in the terminal for assistance in learning more about the game.
5. Note that any depth greater than 3 will result in slow processing times. No default is set.

# CREDIT:

- I'd like to thank the following article from FreeCodeCamp: https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
 for helping me in the development of the A.I. The piece and position evaluation was a big help in developing a working A.I. 
 
 # OTHER:
 
 Chess is an extremely complicated game (in terms of the number of tactics and strategies that can be used), in order to create the most efficient A.I, numerous different types of evaluations are used in addition to tables filled with excellent starting moves. While this A.I I developed is lacking compare to other A.I's individuals have made, I believe that it is a good starting point in my A.I career development. I hope to be able to do more projects like this and constantly improve my programming knowledge and skills.


