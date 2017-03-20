#!/usr/bin/env python

# https://www.codechef.com/COOK80/problems/ROBOTG
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    unsafe
    safe
    unsafe
    safe
    safe
    '''

    return io.StringIO('''5
1 1
R
2 3
LLRU
3 2
LLRU
4 3
ULURUDRDLD
3 6
RURUR''')

def get_input(source):
    '''
    Generates a tuple (N, M, s) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, m = list(map(int, next(lines).strip().split(' ')))
            s = next(lines).strip()

            yield (n, m, s,)

def calc(n, m, s):
    '''
    Returns a boolean.
    '''

    cur_x = 0
    max_x = 0
    min_x = 0
    cur_y = 0
    max_y = 0
    min_y = 0

    for direction in s:
        if direction == 'U':
            cur_y += 1
        elif direction == 'R':
            cur_x += 1
        elif direction == 'D':
            cur_y -= 1
        elif direction == 'L':
            cur_x -= 1

        max_x = max(max_x, cur_x)
        min_x = min(min_x, cur_x)
        max_y = max(max_y, cur_y)
        min_y = min(min_y, cur_y)

    return max_x - min_x < m and max_y - min_y < n

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print('safe' if calc(*args) else 'unsafe')
