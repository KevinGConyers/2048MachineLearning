import tkinter
from logic import *
import random
from puzzle import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Player():
    def __init__(self):

        self.score = 0
        self.goal = 2048

    def play(self, board):
        move = self.scan(board)
        self.move(board, move)


    def scan(self, board):
        if board.matrix[0][0] == 0:
            for i in range(4):
                if board.matrix[0][i] != 0:
                    return LEFT
                if board.matrix[i][0]:
                    return UP
            for i in range(1, 3):
                if board.matrix[i][0] != 0 and board.matrix[i][0] != board.matrix[0][0]:
                    break
                if board.matrix[0][i] != 0 and board.matrix[0][i] != board.matrix[0][0]:
                    break
                if board.matrix[0][0] == board.matrix[0][i]:
                    return LEFT
                if board.matrix[0][0] == board.matrix[i][0]:
                    return UP
        targeti = 0
        targetj = 0
        maxNum = board.matrix[0][0]
        for i in range(4):
            for j in range(4):
                if i == 0 and j == 0:
                    continue
                if board.matrix[i][j] > maxNum:
                    targeti = i
                    targetj = j

        return randint(0, 3)

    def move(self, board, move):
        if move  == 0:
            board.bot_move(KEY_UP)
        if move == 1:
            board.bot_move(KEY_RIGHT)
        if move == 2:
            board.bot_move(KEY_DOWN)
        if move == 3:
            board.bot_move(KEY_LEFT)
