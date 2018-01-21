#!/usr/bin/env python

# https://www.codechef.com/COOK90/problems/SURVIVE
# Submission successful!
import io
import sys

import math

def test_data():
    '''
    Expected output:

    2
    -1
    '''

    return io.StringIO('''2
16 2 10
50 48 7''')

def get_input(source):
    '''
    Generates a tuple of integers (N, K, S) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, k, s = map(int, next(lines).split(' '))

            yield (n, k, s,)

def calc(n, k, s):
    '''
    Returns a number.
    '''

    total_to_eat = k * s
    total_can_buy = n * (s - s // 7)

    return -1 if total_to_eat > total_can_buy else math.ceil(total_to_eat / n)
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
