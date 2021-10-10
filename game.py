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
    None
    #move upwards and rotate matrix for other directions
    #add and return score while adding together two cells
    
        
def GameOver(board):
    None
    #check if any 0 in array then check if any cell is equal with its neighbour