from myCollections import utils as u
from game import Move, GenRandCell, GameOver
from pynput import keyboard
import numpy as np

def on_press(key)->None:
    """Function called by listener. Records keystrokes.

    Args:
        key (pynput.keyboard._win32.KeyCode): w - up, d - right, s - down, a - left.
    """    
    global board
    global score
    try:
        if key.char == 'w':
            u.clear()
            moveTuple = Move(board, 0, score)
            board = moveTuple[0]
            score = moveTuple[1]
            print(board)
            print('Score:', score)
            if GameOver(board):
                u.clear()
                print('GAME OVER')
                print(board)
                print('Score:', score)
                exit()
        if key.char == 's':
            u.clear()
            moveTuple = Move(board, 2, score)
            board = moveTuple[0]
            score = moveTuple[1]
            print(board)
            print('Score:', score)
            if GameOver(board):
                u.clear()
                print('GAME OVER')
                print(board)
                print('Score:', score)
                exit()
        if key.char == 'a':
            u.clear()
            moveTuple = Move(board, 3, score)
            board = moveTuple[0]
            score = moveTuple[1]
            print(board)
            print('Score:', score)
            if GameOver(board):
                u.clear()
                print('GAME OVER')
                print(board)
                print('Score:', score)
                exit()
        if key.char == 'd':
            u.clear()
            moveTuple = Move(board, 1, score)
            board = moveTuple[0]
            score = moveTuple[1]
            print(board)
            print('Score:', score)
            if GameOver(board):
                u.clear()
                print('GAME OVER')
                print(board)
                print('Score:', score)
                exit()
            
        if key.char == 'q':
            exit()
    except AttributeError:
        None

def main()->None:
    global board
    global score
    score = 0
    u.clear()
    board = np.zeros((4,4), int)
    board = GenRandCell(board)
    board = GenRandCell(board)
    print(board)
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

main()