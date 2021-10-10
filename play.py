from myCollections import utils as u
from game import Move, GenRandCell, GameOver
from pynput import keyboard
import numpy as np

def on_press(key):
    global board
    try:
        if key.char == 'w':
            u.clear()
            board = Move(board, 'up')
            print(board)
            GameOver(board)
        if key.char == 's':
            u.clear()
            board = Move(board, 'down')
            print(board)
            GameOver(board)
        if key.char == 'a':
            u.clear()
            board = Move(board, 'left')
            print(board)
            GameOver(board)
        if key.char == 'd':
            u.clear()
            board = Move(board, 'right')
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
    board = GenRandCell(board)
    board = GenRandCell(board)
    print(board)
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

main()