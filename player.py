import tkinter
from logic import *
import random
from puzzle import *



class Player():
    def __init__(self):

        self.score = 0
        self.goal = 2048
        #game.mainloop()
        self.play(game.matrix)

    def play(self, board):
        while(self.score < self.goal):
            self.scan(board)
            self.move(board)


    def scan(self, board):
        x=None

    def move(self, board):
        x = randint(0,3)
        if x == 0:
            up(board)
        if x == 1:
            right(board)
        if x == 2:
            down(board)
        if x==3:
            left(board)


player = Player()
