import numpy as np
from sys import exit

def GenRandCell(board):
    empty = np.where(board==0)
    emptySpaces = list(zip(empty[0], empty[1]))
    if emptySpaces == []:
        return board
    else:
        rand = np.random.randint(0,len(emptySpaces))
        if np.random.randint(0,10) == 0:
            board[emptySpaces[rand][0]][emptySpaces[rand][1]] = 4
        else:
            board[emptySpaces[rand][0]][emptySpaces[rand][1]] = 2
        return board

def Move(board, dir, checkformoves=0):
    moved = False
    if dir == 'up':
        for y in range(4):
            for x in range(4):
                if board[y][x] != 0:
                    for movment in range(1,4):
                        try:
                            if y-movment >= 0:
                                if board[y-movment][x] == 0:
                                    board[y-movment][x] = board[y-movment+1][x]
                                    board[y-movment+1][x] = 0
                                    moved=True
                                if board[y-movment][x] == board[y-movment+1][x]:
                                    board[y-movment][x] += board[y-movment+1][x]
                                    board[y-movment+1][x] = 0
                                    moved=True
                        except IndexError:
                            None
        if moved:
            if checkformoves == 1:
                return GenRandCell(board), moved
            else:
                return GenRandCell(board)
        else:
            if checkformoves == 1:
                return board, moved
            else:
                return board
                                                        
    if dir == 'right':
        for x in range(3, -1, -1):
            for y in range(4):
                if board[y][x] != 0:
                    for movment in range(1,4):
                        try:
                            if x+movment <= 3:
                                if board[y][x+movment] == 0:
                                    board[y][x+movment] = board[y][x+movment-1]
                                    board[y][x+movment-1] = 0
                                    moved = True
                                if board[y][x+movment] == board[y][x+movment-1]:
                                    board[y][x+movment] += board[y][x+movment-1]
                                    board[y][x+movment-1] = 0
                                    moved = True
                        except IndexError:
                            None
        if moved:
            if checkformoves == 1:
                return GenRandCell(board), moved
            else:
                return GenRandCell(board)
        else:
            if checkformoves == 1:
                return board, moved
            else:
                return board

    if dir == 'down':
        for y in range(3, -1, -1):
            for x in range(4):
                if board[y][x] != 0:
                    for movment in range(1,4):
                        try:
                            if y+movment <= 3:
                                if board[y+movment][x] == 0:
                                    board[y+movment][x] = board[y+movment-1][x]
                                    board[y+movment-1][x] = 0
                                    moved=True
                                if board[y+movment][x] == board[y+movment-1][x]:
                                    board[y+movment][x] += board[y+movment-1][x]
                                    board[y+movment-1][x] = 0
                                    moved=True
                        except IndexError:
                            None
        if moved:
            if checkformoves == 1:
                return GenRandCell(board), moved
            else:
                return GenRandCell(board)
        else:
            if checkformoves == 1:
                return board, moved
            else:
                return board

    if dir == 'left':
        for x in range(4):
            for y in range(4):
                if board[y][x] != 0:
                    for movment in range(1,4):
                        try:
                            if x-movment >= 0:
                                if board[y][x-movment] == 0:
                                    board[y][x-movment] = board[y][x-movment+1]
                                    board[y][x-movment+1] = 0
                                    moved = True
                                if board[y][x-movment] == board[y][x-movment+1]:
                                    board[y][x-movment] += board[y][x-movment+1]
                                    board[y][x-movment+1] = 0
                                    moved = True
                        except IndexError:
                            None
        if moved:
            if checkformoves == 1:
                return GenRandCell(board), moved
            else:
                return GenRandCell(board)
        else:
            if checkformoves == 1:
                return board, moved
            else:
                return board
        
def GameOver(board):
    if not(Move(board, 'up', 1)[1]) and not(Move(board, 'left', 1)[1]) and not(Move(board, 'down', 1)[1]) and not(Move(board, 'right', 1)[1]):
        print('Game Over')
    else:
        print('Possible move')