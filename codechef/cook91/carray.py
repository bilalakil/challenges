#!/usr/bin/env python

# https://www.codechef.com/COOK91/problems/CARRAY
# Submission successful! LOLWAT
import io
import sys

def test_data():
    '''
    Expected output:

    3
    '''

    return io.StringIO('''1
5 4 1
100 2 4 17 8''')

def get_input(source):
    '''
    Generates a tuple of integers (N, k, b, A) for each test case,
    where A is a list of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, k, b = map(int, next(lines).split(' '))
            a = list(map(int, next(lines).split(' ')[:n]))

            yield (n, k, b, a,)

def calc(n, k, b, a):
    '''
    Returns an integer.
    '''

    a = sorted(a)

    ans = 1
    cur = k*a[0] + b

    for i in a[1:]:
        if cur <= i:
            ans += 1
            cur = k*i + b

    return ans
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
