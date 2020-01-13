from Player import Player
from Board import Board

class Chess():

    def __init__(self, board, player1, player2):
        turn = False  # False for W, True for B
        self.board = board
        self.player1 = player1
        self.player2 = player1

    def askForSide(self) -> str:
        input("What team would like to play on? Type 'W' for White and 'B' for Black: ")

    def askForDepth(self) -> int:
        input("What depth would like the A.I to compute to? Type an integer: ")
    
    