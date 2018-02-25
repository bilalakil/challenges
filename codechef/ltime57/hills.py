#!/usr/bin/env python

# https://www.codechef.com/LTIME57/problems/HILLS
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    3
    5
    1
    '''

    return io.StringIO('''3
5 3 2
2 5 2 6 3
5 2 3
4 4 4 4 4
5 2 7
1 4 3 2 1''')

def get_input(source):
    '''
    Generates a tuple (N, U, D, H) for each test case,
    where H is a list of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, u, d = map(int, next(lines).strip().split(' '))
            h = list(map(int, next(lines).strip().split(' ')[:n]))

            yield (n, u, d, h,)

def calc(n, u, d, h):
    '''
    Returns an integer.
    '''

    cur = 1
    cur_height = h[0]

    has_parachute = True

    for i in range(1, n):
        height = h[i]

        if height < cur_height - d or height > cur_height + u:
            if height < cur_height and has_parachute:
                has_parachute = False
            else:
                break

        cur += 1
        cur_height = height

    return cur

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
