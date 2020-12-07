import math
import numpy as np

def main():
    f = open("input.txt")
    i = 0
    nHit = 0
    for line in f:
        nCols = len(line)
        modL = list(line)
        if line[i] == '#':
            nHit += 1
            modL[i] = "X"
        else:
            modL[i] = "0"
        print("".join(modL))
        i = (i + 3) % (nCols - 1)
    print(str(nHit))
if __name__ == "__main__":
    main()
