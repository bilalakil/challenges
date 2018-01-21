#!/usr/bin/env python

# https://www.codechef.com/COOK90/problems/MAGA
# Immature solution, wrought with logical error. Looks interesting though :P
import io
import sys

def test_data():
    '''
    Expected output:

    1
    -1
    '''

    return io.StringIO('''2
6
1 2 3 4 5 6
7
1 2 3 4 5 6 7''')

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
    Returns a number.
    '''

    cmps = [(lambda x, y: x < y), (lambda x, y: x > y)]
    flips = 0

    for i in range(n // 2):
        l = cmps[i % 2](a[i], a[i + 1])
        r = cmps[(i + n + 1) % 2](a[n-1 - i], a[n-1 - i - 1])

        if l != r:
            return -1
        elif not l:
            flips += 1

    return min(flips, n // 2 - flips)

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
