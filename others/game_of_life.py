import numpy as np

def game_of_life(board):
    neighbors = sum(np.roll(np.roll(board, i, 0), j, 1)
                    for i in (-1, 0, 1) for j in (-1, 0, 1)
                    if (i != 0 or j != 0))
    return (neighbors == 3) | (board & (neighbors == 2))

def display_board(board):
    print('\n'.join(''.join('⬛' if cell else '⬜' for cell in row) for row in board))
    print('-' * len(board[0]))

board = np.random.randint(2, size=(10, 10))
for _ in range(5):
    display_board(board)
    board = game_of_life(board)