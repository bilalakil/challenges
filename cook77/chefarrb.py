#!/usr/bin/env python3

# https://www.codechef.com/COOK77/problems/CHEFARRB
# Didn't submit calc_backwards in time to see if it'd pass (although I don't think it would've).
# The others timed out.

import io
import random
import sys

from itertools import combinations
from functools import reduce

limit_n = 100000
limit_k = 10 ** 9

def test_data(incl_big, incl_killer):
    '''
    With limits of n = 10 ** 6 and k = 10 ** 9, expected calculations are:

    4
    2
    18
    4999779290
    0

    Or with incl_big = False:

    4
    2
    18
    '''

    s = str(3 + (1 if incl_big else 0) + (1 if incl_killer else 0)) + '''
3 3
1 2 3
3 6
3 4 5
7 3
3 1 1 2 1 1 1
'''

    if incl_big:
        random.seed(1)

        ints = ' '.join([str(random.randint(0, limit_k)) for i in range(limit_n)])
        s += '{n} {k}\n{ints}\n'.format(n=limit_n, k=limit_k, ints=ints)

    if incl_killer:
        s += '{n} {k}\n{ints}\n'.format(n=limit_n, k=limit_k, ints=' '.join(['1' for i in range(limit_n)]))

    return io.StringIO(s)

def get_input(source):
    '''
    Generates a tuple (K, A), where K is an integer and A is a tuple of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, k = map(int, next(lines).split(' '))
            integers = tuple(map(int, next(lines).split(' ')[:n]))

            yield (k, integers,)

def calc(k, integers):
    return calc_backwards(k, integers)

def calc_combinations(k, integers):
    '''
    Loops through every possible slice - naive.
    Slow for large N.

    Returns an integer.
    '''

    result = 0

    for i, j in combinations(range(len(integers) + 1), 2):
        if reduce(lambda x, y: x | y, integers[i:j]) >= k:
            result += 1

    return result

def calc_skip(k, integers):
    '''
    Loops through each position and skips possible calculations.
    If the slice [0:2] is good, then [0:3], [0:4], and such definitely are.

    Slow for many small Ai.

    Returns an integer.
    '''

    n = len(integers) + 1
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            if reduce(lambda x, y: x | y, integers[i:j]) >= k:
                result += n - j
                
                break

    return result

def calc_backwards(k, integers):
    '''
    Loops backwards through the array for a running sum.
    Not sure if backwards is necessary - that's just how the idea came to me.

    Example case:
    7 3
    3 1 1 2 1 1 1

    Iteration:   0 (1)  1 (1)   2 (1)       3 (2)           4 (1)   5 (1)   6 (3)
    Hanging:     [1]    [1, 1]  [1, 1, 1]   [2]             [1]     [1, 1]  []
    Accumulator: +0     +0      +0          +3 [3, 3, 3]    +4 [3]  +4      +7 [3, 3]
    Result:      0      0       0           3               7       11      18

    Slow for many small Ai, otherwise slightly faster than calc_skip.

    Returns an integer.
    '''

    result = 0
    accumulated = 0
    hanging = []

    for i in reversed(integers):
        hanging = list(map(lambda x: x | i, hanging))
        hanging.append(i)

        for j in range(len(hanging), 0, -1):
            if hanging[j - 1] >= k:
                hanging = hanging[j:]
                accumulated += j

                break

        result += accumulated

    return result

if __name__ == '__main__':
    incl_big = '-nobig' not in sys.argv
    incl_killer = '-nokiller' not in sys.argv

    inp = test_data(incl_big, incl_killer) if '-test' in sys.argv else sys.stdin

    f = calc
    if '-1' in sys.argv:
        f = calc_combinations
    elif '-2' in sys.argv:
        f = calc_skip
    elif '-3' in sys.argv:
        f = calc_backwards

    for k, integers in get_input(inp):
        print(f(k, integers))
