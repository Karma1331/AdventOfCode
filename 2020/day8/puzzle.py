#!/usr/bin/python3

# staging
import os
import re
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOTDIR, 'input.txt')

with open(FILE) as f:
    f_raw = f.read()
    f_list = f_raw.split('\n')
    k_list = []
    v_list = []

    for line in f_list:
        k, v = re.split(r' ', line)
        k_list.append(k)
        v_list.append(v)

counter = 0
tracker = []


def InfiniteLoop(i, counter, k_list, v_list, tracker):
    if k_list[i] == 'acc':
        counter += int(v_list[i])
        i += 1
    elif k_list[i] == 'jmp':
        i += int(v_list[i])
    elif k_list[i] == 'nop':
        i += 1

    if i not in tracker:
        tracker.append(i)
        InfiniteLoop(i, counter, k_list, v_list, tracker)
    else:
        print(f'Part 1: {counter}')
        return False


#def LoopBreaker(i, counter, k_list, v_list, tracker):



InfiniteLoop(0, counter, k_list, v_list, tracker)
