import math
import numpy as np

def main():
    f = open("input.txt")
    nCorrectA = 0
    nFalseA = 0

    nCorrectB = 0
    nFalseB = 0


    for line in f:
        [low, rest] = line.split('-')

        [high, rest] = rest.split(' ', 1)
        [reqC, rest] = rest.split(':')
        [_, pw] = rest.split(' ')

        a = pw[int(low) - 1]
        b = pw[int(high) - 1]
        if (a == reqC or b == reqC) and a != b:
            nCorrectB += 1
        else:
            nFalseB += 1

    print("NCorrect: " + str(nCorrectB) + " NFalse " + str(nFalseB))

if __name__ == "__main__":
    main()
