#!/usr/bin/python

# staging
import os
import re
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOTDIR, 'puzzle1-input.txt')

counter = 0

with open(FILE) as f:
    for line in f:
        line = line.strip('\n')

        first, second, char, password = re.split('-| |: ', line)

        if (password[int(first) - 1] == char) ^ (password[int(second) - 1] == char):
            counter += 1
    
    print(counter)