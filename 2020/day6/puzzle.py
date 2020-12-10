#!/usr/bin/python3

# staging
import os
from collections import Counter
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOTDIR, 'input.txt')


def GroupSum(data):
    counter = 0
    subs = data.read() 

    for entry_raw in subs.split('\n\n'):
        entry_san = entry_raw.replace('\n','')
        entry_cnt = len(set(entry_san))

        counter += entry_cnt
    
    return counter


def Common(data):
    counter = 0
    subs = data.read()

    for group in subs.split('\n\n'):
        group_count = group.count('\n') + 1
        group_match = Counter(group.replace('\n',''))

        match_list = [ k for k, v in group_match.items() if v == group_count ]

        counter += len(match_list)
    
    return counter

        
print(f'Part 1: {GroupSum(open(FILE))}')

print(f'Part 2: {Common(open(FILE))}')