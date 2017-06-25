#!/usr/bin/env python

# https://www.codechef.com/LTIME49/problems/TWONMS
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    1
    3
    2
    '''

    return io.StringIO('''3
1 2 1
3 2 3
3 7 2''')

def get_input(source):
    '''
    Generates a tuple (A, B, N) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            a, b, n = map(int, next(lines).split(' '))

            yield (a, b, n,)

def calc(a, b, n):
    '''
    Returns an integer.
    '''

    a = a * (2 if n % 2 == 1 else 1)
    
    x = max(a, b)
    y = min(a, b)

    return x // y

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
