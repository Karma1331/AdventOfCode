#!/usr/bin/python3

# staging
import os
import numpy as np

# Toggle testing
test = 0

if test:
    ROOTDIR = os.path.dirname(os.path.abspath(__file__))
    FILE    = os.path.join(ROOTDIR, 'test.txt')
    PRE     = 5
else:
    ROOTDIR = os.path.dirname(os.path.abspath(__file__))
    FILE    = os.path.join(ROOTDIR, 'input.txt')
    PRE     = 25

# Read & assign file
with open(FILE) as f:
    f_san   = [int(line.strip('\n')) for line in f.readlines()]

# Let the fun begin
def Part1(preamble, items):
    
    # Set pre-run variables
    start   = 0
    stop    = start + preamble
    index   = preamble

    # Not at end yet
    while index < len(items) - 1:
        pool    = items[start:stop]
        flag    = False

        # Remove last char | Check if n1 + n2 == number then break out of if & for loop | Run until Flag's not set to True then return number
        for n1 in pool[:-1]:
            for n2 in pool[1:]:
                if n1 + n2 == items[index]:
                    flag    = True
                    break
            if flag:
                break
        if not flag:
            return items[index]
        
        index   += 1
        start   += 1
        stop    += 1

def Part2(number, items):
    flag    = False

    # Iterate through list
    for i1 in range(0, len(items) - 1):

        # Break back to i1 if sum > number
        while not flag:
            for i2 in range(0, len(items) - 1):
                pool    = np.array(items[i1:i2])

                # If sum equals number, return. Else, keep running until flag is True then break.
                if np.sum(pool) == number:
                    return pool.min() + pool.max()
                elif np.sum(pool) > number:
                    flag    = True
                    break
            if flag:
                flag    = False
                break    


print(f'Part 1: {Part1(PRE, f_san)}')

print(f'Part 2: {Part2(Part1(PRE, f_san), f_san)}')