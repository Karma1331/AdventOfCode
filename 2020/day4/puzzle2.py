#!/usr/bin/python

# staging
import os
import re
ROOTDIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(ROOTDIR, 'input.txt')

count = 0

with open(FILE) as f:

    open_file = f.read()

    raw_batch = open_file.split('\n\n')
    san_batch = [line.replace('\n',' ') for line in raw_batch]

    for passport in san_batch:
              
        if (
            re.search(r'byr:(19[2-9][0-9]|200[0-2])', passport) and
            re.search(r'iyr:(201[0-9]|2020)', passport) and
            re.search(r'eyr:(202[0-9]|2030)', passport) and
            re.search(r'hgt:((?:1[5-8][0-9]|19[0-3])cm|(?:59|6[0-9]|7[0-6])in)', passport) and
            re.search(r'hcl:(\#[\da-f]{6})', passport) and
            re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', passport) and
            re.search(r'pid:([\d]{9})', passport)):

            count += 1
            print(passport)
        
        else:
            print('Not found')
    
    print(count)
        