import math
import numpy as np
import re

class Bag:
    def __init__(self, t):
        self.holds = []
        self.n = []
        self.t = t

def holds(bags, bag, t):
    for b in bag.holds:
        if bags[b].t == t:
            return True
        elif holds(bags, bags[b], t):
            return True
    return False

def ch(bags, bag):
    count = 0
    i = 0
    for b in bag.holds:
        apa = ch(bags, bags[b])
        count += apa * int(bag.n[i])
        count += int(bag.n[i])
        i += 1
    # print(bag.t + " holds " + str(count) + " bags")
    return count

def main():
    f = open("input.txt")
    count = 0
    bags = dict()
    for line in f:
        owner = re.findall(r'(\S+ \S+) bags contain', line)[0]
        bags[owner] = Bag(owner)
        childs = re.findall(r'(\d+ \S+ \S+) bags?[,.]', line)
        for c in childs:
            k = re.findall(r'(\d+) (\S+ \S+)', c)

            n = k[0][0]
            t = k[0][1]
            if int(n) > 0:
                bags[owner].holds.append(t)
                bags[owner].n.append(n)

    for bag in bags:
        if bags[bag].t != 'shiny gold':
            if holds(bags, bags[bag], 'shiny gold'):
                count += 1

    n2 = ch(bags, bags['shiny gold'])

    print(n2)


if __name__ == "__main__":
    main()
