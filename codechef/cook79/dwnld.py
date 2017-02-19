#!/usr/bin/env python

# https://www.codechef.com/COOK79/problems/DWNLD
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    6
    3
    110
    '''

    return io.StringIO('''3
2 2
2 1
2 3
2 2
1 2
2 3
3 0
1 2
2 4
10 10
''')

def get_input(source):
    '''
    Generates a tuple (K, [(T1, D1), ..., (TN, DN)]) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, k = list(map(int, next(lines).split(' ')))
            data = [tuple(list(map(int, next(lines).split(' ')))) for _ in range(n)]

            yield (k, data,)

def calc(k, data):
    price = 0

    for t, d in data:
        price += max(t - k, 0) * d
        k = max(k - t, 0)
    
    return price

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
