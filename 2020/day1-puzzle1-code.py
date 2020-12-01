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

for number in content_san:
    a = int(number)
    b = 2020 - a
    if str(b) in content_san:
        print(f"Answer: {a * b}")