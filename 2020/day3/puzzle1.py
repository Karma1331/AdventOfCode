#!/usr/bin/python

# staging
import os
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOTDIR, 'input.txt')

counter = 0

with open(FILE) as f:

    # create tree matrix
    target_map = [line.split() for line in f]


def CountTree(x, y, tree_map):
    
    row = str(tree_map[0])

    # make sure we're not on last row
    while y < len(tree_map):

        # if at end of row, reposition x
        if x == len(list(tree_map[x])):
            x = -1
        
        # move x and y
        x += 3
        y += 1

        # check if equal to char
        if tree_map[x][y] == '#':
            counter += 1

        CountTree(x, y)
    
    else:
        print(counter)

CountTree(0, 0, target_map)