import math
import numpy as np


def a():
    f = open("input.txt")

    total = 0
    groupMap = np.zeros(ord('z') - ord('a') + 1)
    memberCount = 0
    for line in f:
        subtotal = 0

        if line != "\n":
            memberCount += 1
            for c in line:
                id = ord(c) - ord('a')
                if (id >= 0 and id < ord('z')):
                    groupMap[id] += 1
        else:
            i = 0
            for n in groupMap:
                if n == memberCount:
                    subtotal += 1
                    print("." + chr(i + ord('a')), sep="", end="")
                i += 1
            groupMap = np.zeros(ord('z') - ord('a') + 1)
            memberCount = 0
            print("\nEndGroup")
            print("Group total: " + str(subtotal))
            total += subtotal

    print(total)

def main():
    a()

if __name__ == "__main__":
    main()
