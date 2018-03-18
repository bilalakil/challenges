#!/usr/bin/env python

# https://www.codechef.com/COOK92A/problems/CO92SUBW
# Submitted successfully!
import io
import sys

import math

def test_data():
    '''
    Expected output:

    1
    2
    2
    5
    '''

    return io.StringIO('''4
1
2
3
9''')

def get_input(source):
    '''
    Generates a tuple with a single integer (X) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            x = int(next(lines))

            yield (x,)

def t(n):
    return (n * (n - 1)) // 2

def calc(x):
    '''
    Returns an integer.
    '''

    approx_tri_num = (1 + math.sqrt(1 + 8 * x)) / 2

    low_tri_num = math.floor(approx_tri_num)
    high_tri_num = math.ceil(approx_tri_num)

    closer = low_tri_num if x - t(low_tri_num) <= t(high_tri_num) - x else high_tri_num

    return closer + abs(t(closer) - x) - 1
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
