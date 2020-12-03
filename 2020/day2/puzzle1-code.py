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
        lower, upper, char, password = re.split('-| |: ', line)

        if int(lower) <= password.count(char) <= int(upper):
            counter += 1

print(str(counter))