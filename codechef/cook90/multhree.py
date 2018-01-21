#!/usr/bin/env python

# https://www.codechef.com/COOK90/problems/MULTHREE
# Submission successful! Lots of wasted attempts though ;(
import io
import sys

import math

def test_data(full):
    '''
    Expected output:

    NO
    YES
    YES
    '''

    if not full:
        return io.StringIO('''3
5 3 4
13 8 1
760399384224 5 1''')

    return io.StringIO('90\n' + '\n'.join(['999999999999 {} {}'.format(i // 10, i % 10) for i in range(90)]))

def get_input(source):
    '''
    Generates a tuple of integers (K, D0, D1) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            k, d0, d1 = map(int, next(lines).split(' '))

            yield (k, d0, d1,)

def calc(k, d0, d1):
    '''
    Returns a boolean.
    '''

    start = d0 * 10 + d1
    k -= 2

    nxt = (d0 + d1) % 10

    if nxt in [0, 5]:
        return False

    while k != 0 and nxt not in [2, 4, 6, 8]:
        start = start * 10 + nxt
        nxt = (nxt * 2) % 10
        k -= 1

    if k == 0:
        return start % 3 == 0

    pattern = [2, 4, 8, 6, 2, 4, 8, 6]
    i = pattern.index(nxt)
    pattern = pattern[i:i+4]

    # 2 is the mod of the pattern's sum (20 % 3 = 2)
    cur_mod = start % 3 + 2 * (k // 4)
    k %= 4

    cur_mod += sum(pattern[0:k])

    return cur_mod % 3 == 0
        
if __name__ == '__main__':
    full = '-f' in sys.argv
    inp = test_data(full) if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print('YES' if calc(*args) else 'NO')
