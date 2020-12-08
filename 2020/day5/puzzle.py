#!/usr/bin/python3

# staging
import os
import re
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOTDIR, 'input.txt')

sid_list = []

def Sid(file):

    for line in file:
    
        line = line.strip('\n')
        line = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        row = int(line[0:7],2)
        col = int(line[7:],2)

        sid_list.append(row * 8 + col)
        sid_list.sort()

    return sid_list[-1]


def Missing(list):
    
    return set(range(list[0], list[-1])) - set(list)


print(f'Part 1: {Sid(open(FILE))}')

print(f'Part 2: {Missing(sid_list)}')