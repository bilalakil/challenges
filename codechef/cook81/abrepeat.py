#!/usr/bin/env python

# https://www.codechef.com/COOK81/problems/ABREPEAT
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    6
    2
    64197148392731290
    '''

    return io.StringIO('''3
4 2
abcb
7 1
aayzbaa
12 80123123
abzbabzbazab''')

def get_input(source):
    '''
    Generates a tuple (S, K,) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, k = list(map(int, next(lines).strip().split(' ')))
            s = next(lines).strip()

            yield (s, k,)

def calc(s, k):
    '''
    Returns an integer.
    '''

    diff = []
    bs = 0
    for c in s:
        if c == 'b':
            bs += 1

        diff.append(bs)

    if bs == 0:
        return 0

    tri = k * (k + 1) // 2
    tri_b = bs * tri
    tot = 0
    for i in range(len(s)):
        if s[i] == 'a':
            tot += tri_b - diff[i] * k

    return tot
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
