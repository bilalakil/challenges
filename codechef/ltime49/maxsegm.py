#!/usr/bin/env python

# https://www.codechef.com/LTIME49/problems/MAXSEGM
# Submission successful!
import io
import sys

def test_data():
    '''
    Expected output:

    21
    '''

    return io.StringIO('''1
5
0 1 2 0 2
5 6 7 8 2''')

def get_input(source):
    '''
    Generates a tuple (N, C, W) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            c = list(map(int, next(lines).split(' ')))
            w = list(map(int, next(lines).split(' ')))

            yield (n, c, w,)

def calc(n, c, w):
    '''
    Returns an integer.
    '''

    left = 0
    right = 0
    cur = set()
    ans = -1
    cur_sum = 0

    while right != len(c):
        if c[right] in cur:
            ans = max(ans, cur_sum)
            cur.remove(c[left])
            cur_sum -= w[left]

            left += 1
        else:
            cur.add(c[right])
            cur_sum += w[right]

            right += 1
    
    ans = max(ans, cur_sum)

    return ans

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
