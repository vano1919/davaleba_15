import numpy as np
import matplotlib.pyplot as plt

board = np.zeros((8, 8), dtype=int)

board[1::2, ::2] = 1
board[::2, 1::2] = 1

board[::2, 1::2] = 1
board[1::2, ::2] = 1

fig, ax = plt.subplots()
ax.imshow(board, cmap='binary')

ax.set_xlim([-0.5, 7.5])
ax.set_ylim([-0.5, 7.5])

ax.set_axis_off()

plt.show()
