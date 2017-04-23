#!/usr/bin/env python

# https://www.codechef.com/COOK81/problems/CANDY123
# Submission successful!
import io
import sys

def test_data():
    '''
    Expected output:

    Bob
    Limak
    Limak
    Bob
    Bob
    Limak
    Limak
    Bob
    Bob
    Bob
    '''

    return io.StringIO('''10
3 2
4 2
1 1
1 2
1 3
9 3
9 11
9 12
9 1000
8 11''')

def get_input(source):
    '''
    Generates a tuple (A, B,) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            a, b = list(map(int, next(lines).strip().split(' ')))

            yield (a, b,)

def calc(a, b):
    '''
    Returns a string: 'Bob' or 'Limak'.
    '''

    limak = 0
    bob = 0
    cur = 1

    while True:
        if cur % 2 == 1:
            limak += cur

            if limak > a:
                return 'Bob'
        else:
            bob += cur

            if bob > b:
                return 'Limak'

        cur += 1

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
