import numpy as np

board = np.zeros((8, 8), dtype=int)

board[1::2, ::2] = 1
board[::2, 1::2] = 1

for row in board:
    print(*row)