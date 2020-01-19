from typing import List
import copy

"""
    @desc: The Utility class holds important pieces of data for each piece that exists in the the game of Chess.
        Additionally, it holds methods that all for conversions and data retrieval.
"""
class Utility:

    # A set of the basic moves a piece can make.
    moves = {
        "k": [[0,1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [-2, 0], [2, 0]],
        "r" : [
            [0,1], [1, 0], [0, -1], [-1, 0], 
            [0,2], [2, 0], [0, -2], [-2, 0], 
            [0,3], [3, 0], [0, -3], [-3, 0], 
            [0,4], [4, 0], [0, -4], [-4, 0], 
            [0,5], [5, 0], [0, -5], [-5, 0], 
            [0,6], [6, 0], [0, -6], [-6, 0], 
            [0,7], [7, 0], [0, -7], [-7, 0]],
        "b" : [
            [1, 1], [1, -1], [-1, 1], [-1, -1],
            [2, 2], [2, -2], [-2, 2], [-2, -2],
            [3, 3], [3, -2], [-3, 3], [-3, -3],
            [4, 4], [4, -4], [-4, 4], [-4, -4],
            [5, 5], [5, -5], [-5, 5], [-5, -5],
            [6, 6], [6, -6], [-6, 6], [-6, -6],
            [7, 7], [7, -7], [-7, 7], [-7, -7]],
        "n" : [[1, 2], [1, -2], [-1, 2], [-1, -2,], [2, 1], [2, -1], [-2, 1], [-2, -1]],
        "p" : [[0, 1], [0, 2], [1, 1], [-1, 1]],
    }

    # The queen can make the moves a Bishop and Rook can make.
    moves["q"] = moves["b"] + moves["r"]

    # The values of pieces on the white team, negated if team is black.
    values = {
        "k" : 900,
        "q" : 90,
        "r" : 50,
        "b" : 30,
        "n" : 30,
        "p" : 10
    }

    # A list of the unicodes for the white team.
    whiteIcons = {
        "k" : "\u265A",
        "q" : "\u265B",
        "r" : "\u265C",
        "b" : "\u265D",
        "n" : "\u265E",
        "p" : "\u265F"
    }

    # A list of unicodes for the black team.
    blackIcons = {
        "k" : "\u2654",
        "q" : "\u2655",
        "r" : "\u2656",
        "b" : "\u2657",
        "n" : "\u2658",
        "p" : "\u2659"
    }

    # A list of position evaluations for each piece on the white team. Inverse if team is black.
    positionValues = {
        "k": [
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
        [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
        [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
        [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]],

        "q": [
        [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
        [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
        [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]],

         "r": [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]],

        "b": [
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
        [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
        [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
        [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
        [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
        [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]],
       
        "n": [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]],

        "p": [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]],
        
    }

    """
        @desc: Converts character to integer.
        @param str: A lower case string from 'a' - 'h'.
        @return Integer: Returns the corresponding integer from 0 - 7.
    """
    @staticmethod
    def convertToNumber(letter: str) -> int:
        return ord(letter) - 97

    """
        @desc: Converts integer to string.
        @param number: A number from 0-7.
        @param String: Returns the corresponding string from 'a' - 'h'.
    """
    @staticmethod
    def convertToLetter(number: int) -> chr:
        return chr(number + 97)

    """
        @desc: Converts a string move into a list of integers.
        @param move: The string move.
        @return List: A list of integers.
    """
    @staticmethod
    def convertStringMoveToInt(move: str) -> List[int]:
        moves = []

        for char in range(len(move)):
            if char % 2 == 0:
                moves.append(Utility.convertToNumber(move[char]))
            else:
                moves.append(int(move[char]) - 1)

        return moves

    """
        @desc: Converts a list of integers into a string move.
        @param move: The list of integers to convert.
        @return String: A string holding a possible valid move.
    """
    @staticmethod
    def convertIntMoveToString(move: List[int]) -> str:
        moves = ""

        for char in range(len(move)):
            if char % 2 == 0:
                moves += Utility.convertToLetter(move[char])
            else:
                moves += str(move[char] + 1)

        return moves

    """
        @desc: Makes all the values in a list negative and returns it.
        @param array: The list to convert.
        @return List: The negated list.
    """
    @staticmethod
    def negateArray(array: List[List[int]]) -> List[List[int]]:

        negativeArray = copy.deepcopy(array)

        for row in range(len(array)):
            for column in range(len(array[row])):
                negativeArray[row][column] *= -1

        return negativeArray

    """
        @desc: Inverses an array.
        @return List: Returns the inverted list.
    """
    @staticmethod
    def inverseArray(array: List[List[int]]) -> List[List[int]]:
        return list(reversed(array))

    """
        @desc: Retrieves the list of basic moves for a given piece.
        @param team: The team of the piece.
        @param name: The name of the piece.
        @return List: The list of all moves that can be made.
    """
    @staticmethod
    def getBasicMoves(team: chr, name: chr) -> List[List[int]]:

        if team == "W":
            return Utility.moves[name]
        else:
            return Utility.negateArray(Utility.moves[name])

    """
        @desc: Retrieves the worth of a piece.
        @param team: The team of the piece.
        @param name: The name of the piece.
        @return Integer: The worth of the piece.
    """
    @staticmethod
    def getPieceEvaluation(team: chr, name: chr) -> int:

        if team == "W":
            return Utility.values[name]
        else:
            return -Utility.values[name]

    """
        @desc: Retrieves the worth of a position depending on what piece is located at (x,y).
        @param team: The team of the piece.
        @param name: The name of the piece.
        @param x: The horizontal location of the piece.
        @param y: The vertical location of the piece.
    """
    @staticmethod
    def getPositionEvaluation(team: chr, name: chr, x: int, y: int) -> int:

        if team == "W":
            return (Utility.positionValues[name])[y][x]
        else:
            return (Utility.negateArray(Utility.inverseArray(Utility.positionValues[name])))[y][x]

    """
        @desc: Retrieves the unicode for a piece.
        @param team: The team to which the piece belongs to.
        @param name: The name of the piece.
        @return String: The unicode of the piece.
    """
    @staticmethod
    def getPieceIcon(team: chr, name: chr) -> str:

        if team == "W":
            return Utility.whiteIcons[name]
        else:
            return Utility.blackIcons[name]
