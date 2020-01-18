from typing import List
import copy

class Utility:

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

    moves["q"] = moves["b"] + moves["r"]

    values = {
        "k" : 900,
        "q" : 90,
        "r" : 50,
        "b" : 30,
        "n" : 30,
        "p" : 10
    }

    whiteIcons = {
        "k" : "\u265A",
        "q" : "\u265B",
        "r" : "\u265C",
        "b" : "\u265D",
        "n" : "\u265E",
        "p" : "\u265F"
    }

    blackIcons = {
        "k" : "\u2654",
        "q" : "\u2655",
        "r" : "\u2656",
        "b" : "\u2657",
        "n" : "\u2658",
        "p" : "\u2659"
    }

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

    ## Set of position evaluation.
    @staticmethod
    def convertToNumber(letter: str) -> int:
        return ord(letter) - 97

    @staticmethod
    def convertToLetter(number: int) -> chr:
        return chr(number + 97)

    @staticmethod
    def convertStringMoveToInt(move: str) -> List[int]:
        moves = []

        for char in range(len(move)):
            if char % 2 == 0:
                moves.append(Utility.convertToNumber(move[char]))
            else:
                moves.append(int(move[char]) - 1)

        return moves

    @staticmethod
    def convertIntMoveToString(move: List[int]) -> str:
        moves = ""

        for char in range(len(move)):
            if char % 2 == 0:
                moves += Utility.convertToLetter(move[char])
            else:
                moves += str(move[char] + 1)

        return moves

    @staticmethod
    def negateArray(array: List[List[int]]) -> List[List[int]]:

        negativeArray = copy.deepcopy(array)

        for row in range(len(array)):
            for column in range(len(array[row])):
                negativeArray[row][column] *= -1

        return negativeArray

    @staticmethod
    def inverseArray(array: List[List[int]]) -> List[List[int]]:
        return list(reversed(array))

    @staticmethod
    def getBasicMoves(team: chr, name: chr) -> List[List[int]]:

        if team == "W":
            return Utility.moves[name]
        else:
            return Utility.negateArray(Utility.moves[name])

    @staticmethod
    def getPieceEvaluation(team: chr, name: chr) -> int:

        if team == "W":
            return Utility.values[name]
        else:
            return -Utility.values[name]

    @staticmethod
    def getPositionEvaluation(team: chr, name: chr, x: int, y: int) -> int:

        if team == "W":
            return (Utility.positionValues[name])[y][x]
        else:
            return (Utility.negateArray(Utility.inverseArray(Utility.positionValues[name])))[y][x]

    @staticmethod
    def getPieceIcon(team: chr, name: chr) -> str:

        if team == "W":
            return Utility.whiteIcons[name]
        else:
            return Utility.blackIcons[name]
