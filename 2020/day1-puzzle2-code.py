#!/usr/bin/env python3

# set path variables
import os
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOTDIR, 'day1-puzzle1-input')

# import data
data_in = open(FILE, "r")
content_raw = data_in.readlines()
data_in.close()

# sanitize data
content_san = [line.rstrip('\n') for line in content_raw]


def n1n2n3(a, target):

    a = list(map(int, a))
    a.sort()

    for i1 in range(0, len(a)-2):
        i2 = i1 + 1
        i3 = len(a) - 1

        f = a[i1]
        m = a[i2]
        l = a[i3]

        while i2 < i3:

            if a[i1] + a[i2] + a[i3] == target:
                print(f"Answer: {a[i1] * a[i2] * a[i3]}")
                return True
            elif a[i1] + a[i2] + a[i3] < target:
                i2 += 1
            else:
                i3 -= 1
        
    return False


a      = content_san
target = 2020

n1n2n3(a, target)