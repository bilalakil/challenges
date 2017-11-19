#!/usr/bin/env python

# https://www.codechef.com/COOK88/problems/RNDPAIR
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    1.00000000
    0.20000000
    0.33333333
    '''

    return io.StringIO('''3
4
3 3 3 3
6
1 1 1 2 2 2
4
1 2 2 3''')

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

def calc_convoluted(n, a):
    '''
    Returns a number.

    Not sure why this is wrong :P Statistics fail!
    '''

    maxes_are_different = False
    prev_max_count = 0
    cur_max = 0
    max_count = 0

    for i in a:
        if i > cur_max:
            prev_max_count = max_count
            maxes_are_different = True

            cur_max = i
            max_count = 0

        if i == cur_max:
            max_count += 1

            if max_count > 1:
                prev_max_count = max_count - 1
                maxes_are_different = False

    return max_count / n * prev_max_count / (n - 1) * (2 if maxes_are_different else 1)

def calc(n, a):
    '''
    Returns a number.
    '''

    cur_max = 0
    max_count = 0

    for i in range(n):
        for j in range(n):
            if i == j: continue

            cur = a[i] + a[j]

            if cur > cur_max:
                cur_max = cur
                max_count = 0

            if cur == cur_max:
                max_count += 1

    return max_count / (n * (n - 1))
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
