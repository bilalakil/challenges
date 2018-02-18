#!/usr/bin/env python

# https://www.codechef.com/COOK91/problems/CCOOK
# Submitted successfully.
import io
import sys

import math

def test_data():
    '''
    Expected output:

    Beginner
    Middle Developer
    Junior Developer
    Jeff Dean
    Senior Developer
    Hacker
    Hacker
    '''

    return io.StringIO('''7
0 0 0 0 0
0 1 0 1 0
0 0 1 0 0
1 1 1 1 1
0 1 1 1 0
0 1 1 1 1
1 1 1 1 0''')

def get_input(source):
    '''
    Generates a list of integers for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            ints = list(map(int, next(lines).split(' ')))

            yield (ints,)

def calc(ints):
    '''
    Returns a string.
    '''

    return ["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean"][sum(ints)]
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
