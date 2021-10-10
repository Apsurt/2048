import sys
import numpy as np
from pynput import keyboard
from sys import exit
from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

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

def Move(board, dir):
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
            return GenRandCell(board)
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
            return GenRandCell(board)
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
            return GenRandCell(board)
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
            return GenRandCell(board)
        else:
            return board
        
def GameOver(board):
    if board == Move(board,'up') and board == Move(board,'down') and board == Move(board,'left') and board == Move(board,'right') and board == Move:
        clear()
        print('Game over')
        print(board)
        exit()

global board
board = np.zeros((4,4), int)
#board = GenRandCell(board)
#board = GenRandCell(board)
board[0][0] = 2
board[0][1] = 2
board[0][2] = 4
board[0][3] = 4
print(board)
#board = Move(board,'right')
#print()
#print(board)

def on_press(key):
    global board
    try:
        if key.char == 'w':
            clear()
            board = Move(board, 'up')
            print(board)
            #GameOver(board)
        if key.char == 's':
            clear()
            board = Move(board, 'down')
            print(board)
            #GameOver(board)
        if key.char == 'a':
            clear()
            board = Move(board, 'left')
            print(board)
            #GameOver(board)
        if key.char == 'd':
            clear()
            board = Move(board, 'right')
            print(board)
            #GameOver(board)
            
        if key.char == 'q':
            exit()
    except AttributeError:
        None

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()