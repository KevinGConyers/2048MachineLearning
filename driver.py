#! /bin/env python3

from player import *
from puzzle import *
from logic import *

player = Player()
game = GameGrid()

while(game_state(game.matrix) == 0):
    game.update()
    player.play(game)

if (game_state(game.matrix) == 1):
    print("win")
else:
    print("lose")

game.mainloop()
