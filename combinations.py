#0-up
#1-right
#2-down
#3-left

def AppendDirs(array)->list[list]:
    """Returns given array with appended all possible combinations of move.

    Args:
        array (list[list]): Every element of the list will be appended 4 times with numbers 0-4.

    Returns:
        appendedArray (list[list]): Appended lists.
    """    
    set = []
    for listIndex in range(len(array)):
        for direction in range(4):
            set.append(array[listIndex].copy())
            set[direction+4*listIndex].append(direction)
    return set

def GenerateCombinations(depth)->list[list]:
    """Returns all combinations of the given depth/lenght.

    Args:
        depth (int): Set how deep/long should the sequences be.

    Returns:
        combinations (list[list]): List of sequences.
    """    
    combinations = [[]]
    for depth in range(depth):
        combinations = AppendDirs(combinations)
    return combinations