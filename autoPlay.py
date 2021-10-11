from myCollections import utils as u
from combinations import *
from game import *

def PrintData(board, score, sequence, moveCap, move, printFreq):
    if printFreq != 0:
        if move%printFreq == 0:
            u.clear()
            print('Current sequence:', *sequence)
            print(board)
            print('Score:',score)
            print('Move:',move)
            if moveCap != None:
                print('Progress:', str(round((((move)/moveCap)*100),2))+'%')

def Blocked(boardBefore):  
    return True
    #TBA for now use moveCap or scoreGoal

def PlaySequence(sequences, moveCap = None, scoreGoal = None, printFreq = 0):
    if scoreGoal is None:
        scoreGoal = 10000000
    if moveCap is None:
        moveCap = 10000000
    board = np.zeros((4,4), int)
    board = GenRandCell(board)
    board = GenRandCell(board)
    score = 0
    move = 0
    while not(GameOver(board)) and Blocked(board) and score <= scoreGoal and move <= moveCap-1:
        moveTuple = Move(board, sequences[move%len(sequences)], score)
        board = moveTuple[0]
        score = moveTuple[1]
        move += 1
        PrintData(board, score, sequences, moveCap, move, printFreq)
    PrintData(board, score, sequences, moveCap, move, printFreq=1)
    return score, move, board
