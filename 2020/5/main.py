import math
import numpy as np

def apa(low, high, c):
    if c == 'R' or c == 'B':
        return [math.floor((low + high)/ 2) + 1, high]
    elif c == 'L' or c == 'F':
        return [low, math.floor((low + high)/ 2)]


def calcSeat(low, high, seatRaw):
    c = seatRaw[0]
    range = apa(low, high, c)
    if ( len(seatRaw) > 1):
        if (range[0] != range[1]):
            return calcSeat(range[0], range[1], seatRaw[1:])
        else:
            return range[0]
    else:
        return range[0]


def main():
    f = open("input.txt")
    max = 128 * 8
    takenSeats = np.arange(max)


    for seatRaw in f:

        # if len(seatRaw) < 6:
        #     continue
        y = seatRaw[0:7]
        x = seatRaw[7:10]
        row = calcSeat(0, 127, y)
        seat = calcSeat(0, 7, x)
        id = row * 8 + seat
        takenSeats[id] = -1

    i = 0
    for seat in takenSeats:

        if seat != -1:
            print("F", sep="", end="")
        else:
            print("-", sep="", end="")
        if i % 8 == 7:
            print("\n" + str(math.floor((i + 1)/8)) + "(" + str(i+1) + "-" + str(i + 8) + ")" + "\t\t", sep="", end="")
        i += 1


if __name__ == "__main__":
    main()
