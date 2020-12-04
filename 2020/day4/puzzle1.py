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
            re.search(r'byr:', passport) and
            re.search(r'iyr:', passport) and
            re.search(r'eyr:', passport) and
            re.search(r'hgt:', passport) and
            re.search(r'hcl:', passport) and
            re.search(r'ecl:', passport) and
            re.search(r'pid:', passport)):
            
            count += 1
        
        else:
            print('Not found')
    
    print(count)
        