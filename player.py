import tkinter
from logic import *
import random
from puzzle import *


class Player():
    def __init__(self):

        self.score = 0
        self.goal = 2048
        #game.mainloop()

    def play(self, board):
        self.scan(board)
        self.move(board)


    def scan(self, board):
        x=None

    def move(self, board):
        x = randint(0,3)
        if x == 0:
            board.commands[KEY_UP]
        if x == 1:
            board.commands[KEY_RIGHT]
        if x == 2:
            board.commands[KEY_DOWN]
        if x==3:
            board.commands[KEY_LEFT]
