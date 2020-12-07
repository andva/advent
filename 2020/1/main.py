import math
import numpy as np

def main():
    f = open("input.txt")
    numbers = []
    for line in f:
        if (int(line) < 2020):
            numbers.append(int(line))
    for n in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n + n2 + n3 == 2020:
                    print(n * n2 * n3)

if __name__ == "__main__":
    main()
