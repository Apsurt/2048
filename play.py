from myCollections import utils as u
from game import Move, GenRandCell, GameOver
from pynput import keyboard
import numpy as np

def on_press(key):
    global board
    try:
        if key.char == 'w':
            u.clear()
            board = Move(board, 0)
            print(board)
            GameOver(board)
        if key.char == 's':
            u.clear()
            board = Move(board, 2)
            print(board)
            GameOver(board)
        if key.char == 'a':
            u.clear()
            board = Move(board, 3)
            print(board)
            GameOver(board)
        if key.char == 'd':
            u.clear()
            board = Move(board, 1)
            print(board)
            GameOver(board)
            
        if key.char == 'q':
            exit()
    except AttributeError:
        None

def main():
    global board
    u.clear()
    board = np.zeros((4,4), int)
    board[0][0] = 2
    board[1][0] = 2
    board[2][0] = 4

    #board = GenRandCell(board)
    #board = GenRandCell(board)
    print(board)
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

main()