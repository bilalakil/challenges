#!/usr/bin/env python

# https://www.codechef.com/LTIME44/problems/NOTINCOM
# Passed.

import io
import sys

def test_data():
    '''
    Expected results:

    1
    0
    '''

    return io.StringIO(
'''2
3 4
1 2 3
3 4 5 6
3 3
1 2 3
4 5 6
'''
    )

def get_input(source):
    '''
    Generates a tuple with two sets of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, m = map(int, next(lines).split(' '))
            a = set(map(int, next(lines).split(' ')[:n]))
            b = set(map(int, next(lines).split(' ')[:m]))

            yield (a, b)

def calc(a, b):
    '''
    Returns an integer.
    '''

    return len(a & b)

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for a, b in get_input(inp):
        print(calc(a, b))
