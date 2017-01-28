#!/usr/bin/env python

# https://www.codechef.com/COOK77/problems/CHEFSETC
# Passed.

import io
import sys

from itertools import permutations

num_integers = 4

def test_data():
    '''
    Expected calculations:

    Yes
    Yes
    No
    Yes
    Yes
    '''

    return io.StringIO(
'''5
1 2 0 3
1 2 4 -1
1 2 3 4
1 2 3 -6
1 5 -2 -3
'''
    )

def get_input(source):
    '''
    Generates tuples of four integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            integers = tuple(map(int, next(lines).split(' ')[:num_integers]))
            yield integers

def calc(integers):
    '''
    Returns True or False.
    '''

    sums = {};

    for i in range(num_integers - 1):
        for ints in permutations(integers, i):
            n = sum(ints)

            if -n in sums:
                return True

            sums[n] = True

    return False

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for integers in get_input(inp):
        print('Yes' if calc(integers) else 'No')
