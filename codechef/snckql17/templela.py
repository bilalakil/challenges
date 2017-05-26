#!/usr/bin/env python

# https://www.codechef.com/SNCKQL17/problems/TEMPLELA
# Submission successful!

import io
import sys

def test_data():
    '''
    Expected answers:

    yes
    no
    no
    no
    yes
    no
    no
    '''

    return io.StringIO('''7
5
1 2 3 2 1
7
2 3 4 5 4 3 2
5
1 2 3 4 3
5
1 3 5 3 1
7
1 2 3 4 3 2 1
4
1 2 3 2
4
1 2 2 1''')

def get_input(source):
    '''
    Returns a tuple (S, strip).
    '''

    with source as lines:
        t = int(next(lines))

        for _ in range(t):
            s = int(next(lines))
            strip = list(map(int, next(lines).strip().split(' ')))

            yield (s, strip,)

def ljhooker(s, strip):
    if s % 2 == 0:
        return False

    mid = (s - 1) / 2

    for i in range(s):
        if i <= mid:
            expected_height = i + 1
        else:
            expected_height = 2 * mid - i + 1
 
        actual_height = strip[i]

        if expected_height != actual_height:
            return False

    return True

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print('yes' if ljhooker(*args) else 'no')

