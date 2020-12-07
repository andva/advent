import math
import numpy as np
import re

def byr(byr):
    try:
        return len(byr) == 4 and int(byr) > 1919 and int(byr) < 2003
    except:
        return False

def iyr(x):
    try:
        return len(x) == 4 and int(x) >= 2010 and int(x) <= 2020
    except:
        return False

def eyr(x):
    try:
        return len(x) == 4 and int(x) > 2019 and int(x) < 2031
    except:
        return False

def hgt(x):
    if x.find('cm') != -1:
        h = x[0:x.find('cm')]
        try:
            return int(h) >= 150 and int(h) <= 193
        except:
            False
    elif x.find('in') != -1:
        h = x[0:x.find('in')]
        try:
            return int(h) >= 59 and int(h) <= 76
        except:
            False

def hcl(x):
    try:
        return x[0] == '#' and len(x[1:]) == 6
    except:
        return False

def ecl(x):
    return x == 'amb' or x == 'blu' or x == 'brn' or x == 'gry' or x == 'grn' or x == 'hzl' or x == 'oth'

def pid(x):
    try:
        return len(x) == 9 and int(x)
    except:
        return False

def verify(pp):
    if ('byr' not in pp
        or 'iyr' not in pp
        or 'eyr' not in pp
        or 'hgt' not in pp
        or 'hcl' not in pp
        or 'ecl' not in pp
        or 'pid' not in pp
        #or 'cid' not in pp
        ):
        return 0
    if (not byr(pp.get('byr')) or 
        not iyr(pp.get('iyr')) or
        not eyr(pp.get('eyr')) or
        not hgt(pp.get('hgt')) or
        not hcl(pp.get('hcl')) or
        not ecl(pp.get('ecl')) or
        not pid(pp.get('pid'))):
        return 0
    return 1


def main():
    f = open("input.txt")

    cPass = dict()
    valid = 0
    for line in f:
        if line == "\n":
            valid += verify(cPass)
            cPass = dict()
        else:
            d = dict(re.findall(r'(\S+):(".*?"|\S+)', line))
            cPass = {**cPass, **d}

    print(str(valid))


if __name__ == "__main__":
    main()
