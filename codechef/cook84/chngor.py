#!/usr/bin/env python

# https://www.codechef.com/COOK84/problems/CHNGOR
# Successfully submitted!
import io
import sys

from itertools import chain

def test_data():
    '''
    Expected output:

    3
    '''

    return io.StringIO('''1
2
1 2''')

def get_input(source):
    '''
    Generates a tuple (N, A) for each test case.
    A is a list of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            a = list(map(int, next(lines).split(' ')[:n]))

            yield (n, a,)

def calc(n, a):
    '''
    Returns an integer.
    '''

    res = 0

    for i in a:
        res |= i

    return res
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
