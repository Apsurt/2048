#0-up
#1-left
#2-down
#3-right

def AppendDirs(array):
    set = []
    for listIndex in range(len(array)):
        for direction in range(4):
            set.append(array[listIndex].copy())
            set[direction+4*listIndex].append(direction)
    return set


def GenerateCombinations(depth):
    combinations = [[]]
    for depth in range(depth):
        combinations = AppendDirs(combinations)
    return combinations

def main():
    b = GenerateCombinations(8)

if __name__ == '__main__':
    main()