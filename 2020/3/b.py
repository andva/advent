import math
import numpy as np

def do(right, down):
    f = open("input.txt")
    i = 0
    n = 0
    nHit = 0
    for line in f:
        if (down > 1 and (n) % down == (down - 1)):
            n += 1
            continue
        nCols = len(line)
        modL = list(line)
        if line[i] == '#':
            nHit += 1
            modL[i] = "X"
        else:
            modL[i] = "0"
        print("".join(modL))
        i = (i + right) % (nCols - 1)
        n += 1
    return nHit

def main():

    total = do(1, 1) * do(3, 1) * do(5, 1) * do(7, 1) * do(1, 2)

    print(total)

if __name__ == "__main__":
    main()
