#!/usr/bin/env python

# https://www.codechef.com/COOK84/problems/CHNGFUNC
# Submitted, but wrong. Not sure why.
# Simplified it and it worked. Still not sure where the convoluted version went wrong.
import io
import sys

import math

def test_data():
    '''
    Expected output:

    46
    '''

    return io.StringIO('''7 100''')

def get_input(source):
    '''
    Generates a tuple (N, A) for each test case.
    A is a list of integers.
    '''

    with source as lines:
        a, b = map(int, next(lines).split(' '))

        return a, b

def calc(a, b):
    '''
    Returns an integer.
    '''

    return sum(math.floor(math.sqrt(x ** 2 + b)) - x for x in range(1, a + 1))

def calc_convoluted(a, b):
    '''
    Returns an integer.
    '''

    c = math.floor(math.sqrt(b + 1)) + 1
    n = c - 2
    total = n

    for x in range(2, a + 1):
        n -= 1

        if b + x ** 2 > c ** 2:
            c += 1
            n += 1

        if n == 0:
            break

        total += n

    return total
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    print(calc(*get_input(inp)))
