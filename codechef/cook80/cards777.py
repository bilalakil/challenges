#!/usr/bin/env python

# https://www.codechef.com/COOK80/problems/CARDS777
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    2.0000000000
    1.0000000000
    2.2000000000
    14.4482758621
    100000.0000000000
    '''

    return io.StringIO('''5
3 1 2
1 6 7
2 3 4
15 14 13
100000 100000 0''')

def get_input(source):
    '''
    Generates a tuple (r, b, p) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            r, b, p = list(map(int, next(lines).split(' ')))

            yield (r, b, p,)

def calc(r, b, p):
    '''
    Returns a number.
    '''

    t = r + b

    return p * (r / t) + (t - p) * (b / t)

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
