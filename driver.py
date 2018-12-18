#! /bin/env python3

from player import *
from puzzle import *
from logic import *

player = Player()
game = GameGrid()

while(true):
    player.play(game.matrix)
