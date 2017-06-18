#!/usr/bin/env python

# https://www.codechef.com/COOK83/problems/KNICOV
# Wrong answer.
#
# Description of why it's wrong found
# [here](https://discuss.codechef.com/questions/102406/knicov-june-cook-off/102413).
# We didn't cover that extra special case for n == 3.
# However even that special case didn't make much sense to me, so I asked about it
# [here](https://discuss.codechef.com/questions/102406/knicov-june-cook-off/102438).
import io
import sys

def test_data():
    '''
    Expected output:

    4
    1
    8
    6
    4
    4
    4
    8
    8
    8
    8
    10
    12
    10
    6
    4
    12
    '''

    return io.StringIO('''2
2 4
1 1
2 8 
2 7
2 6
2 5
2 4
2 9
2 10
2 11
2 12
2 13
2 14
3 13
3 7
3 4
3 14''')

def get_input(source):
    '''
    Generates a tuple (N, M) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, m = map(int, next(lines).split(' '))

            yield (n, m,)

def calc(n, m):
    '''
    Returns an integer.
    '''

    if n == 1:
        return m
    elif m == 1:
        return n
    elif m < 7:
        return 4

    r = m % 6
    if r == 0:
        extra = 0
    elif r == 1:
        extra = 2
    else:
        extra = 4

    return 4 * (m // 6) + extra
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
