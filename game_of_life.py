from pyp5js import *
from random import randrange

import numpy as np

w = 20
columns = None
rows = None
board = None
next_board = None
next = None

def setup():
    js.window.createCanvas(300, 300)
    global next, columns, rows, board, next_board
    # Set simulation frame rate to 10 to avoid flickering
    js.window.frameRate(1)
    columns = 10
    rows = 10
    # Wacky way to make a 2D array in Python
    board = np.zeros((columns, rows), dtype=np.object)
    next_board = np.zeros((columns, rows), dtype=np.object)

    # Fill board randomly
    for i in range(columns):
        for j in range(rows):
            # Lining the edges with 0s
            if i == 0 or j == 0 or i == columns - 1 or j == rows - 1:
                board[i][j] = 0
            # Filling the rest randomly
            else:
                board[i][j] = js.window.floor(randrange(2))
            next = [[0 for j in range(rows)] for i in range(columns)]

def draw():
    global columns, rows, board, next_board
    js.window.background(255)
    generate()
    a = 0
    b = 0
    for i in range(columns):
        for j in range(rows):
            if board[i][j] == 1:
                print('black', a)
                a += 1
                js.window.fill(0)
            else:
                js.window.fill(255)
                b += 1
                print('white', b)
            js.window.stroke(0)
            js.window.rect(i * w, j * w, w-1, w-1)


# The process of creating the new generation
def generate():
    global next, columns, rows, board, next_board
    # Loop through every spot in our 2D array and check spots neighbors
    for x in range(1, columns - 1):
        for y in range(1, rows - 1):
            # Add up all the states in a 3x3 surrounding grid
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    xi = x+i
                    yj = y+j
                    aux = board[xi][yj]
                    neighbors = neighbors + aux

            # A little trick to subtract the current cell's state since
            # we added it in the above loop
            neighbors -= board[x][y]
            # Rules of Life
            if board[x][y] == 1 and neighbors < 2:
                next[x][y] = 0 # Loneliness
            elif board[x][y] == 1 and neighbors > 3:
                next[x][y] = 0 # Overpopulation
            elif board[x][y] == 0 and neighbors == 3:
                next[x][y] = 1 # Reproduction
            else:
                next[x][y] = board[x][y] # Stasis

            temp = board;
            board = next;
            next = temp;

setup()
while (True):
  draw()