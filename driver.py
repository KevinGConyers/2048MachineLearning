#! /bin/env python3

from player import *
from puzzle import *
from logic import *

player = Player()
game = GameGrid()

while(1>0):
    game.update()
    player.play(game)
