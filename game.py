import numpy as np
from sys import exit

def GenRandCell(board):    
    """Returns board with cell generated in random spot.

    Args:
        board (list[list]): Board in which are cells generated.

    Returns:
        board (list[list]): board with cell generated in random spot.
    """    
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

def Move(board, dir, score)->np.ndarray:
    """Takes 2048 board and moves it to the given side.

    Args:
        board (numpy.ndarray): Board state which you wish to move in certain direction.
        dir (int): Sets direction in which the movement will occur (0 - up, 1 - right, 2 - down, 3 - left).

    Returns:
        board (numpy.ndarray): Board state after move.
    """    
    #rotate board
    board = np.rot90(board, dir)
    #find occupied spaces
    notEmpty = np.where(board!=0)
    occupiedSpaces = list(zip(notEmpty[0], notEmpty[1]))
    #creat bools lists (if cell is on the list it is considered as true)
    movedCells = []
    mergedCells = []
    #make a move
    for cell in occupiedSpaces:
        y = cell[0].copy()
        x = cell[1].copy()
        for move in range(1, cell[0]+1):
            if y - move >= 0:
                if board[y-move][x] == 0:
                    board[y-move][x] = board[y-move+1][x]
                    board[y-move+1][x] = 0
                    movedCells.append((y-move, x))
                if (board[y-move][x] == board[y-move+1][x]) and not((y-move+1, x) in mergedCells) and not((y-move, x) in mergedCells):
                    board[y-move][x] += board[y-move+1][x]
                    board[y-move+1][x] = 0
                    score += board[y-move][x]
                    movedCells.append((y-move, x))
                    mergedCells.append((y-move, x))
    #rerotate board
    board = np.rot90(board, 4-dir)
    if movedCells == []:
        return board, score
    else:
        return GenRandCell(board), score
        
def GameOver(board):
    None
    #check if any 0 in array then check if any cell is equal with its neighbour