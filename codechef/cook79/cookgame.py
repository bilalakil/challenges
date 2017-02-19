#!/usr/bin/env python

# https://www.codechef.com/COOK79/problems/COOKGAME
# Solved successfully, but 6 minutes late. Burn.
import io
import sys

def test_data(limit_n):
    '''
    Expected output:

    2
    0
    1
    0
    0
    4
    8
    32
    303861760
    '''

    s = '''9
6
1 1 2 -1 -1 2
3
-1 3 1
4
-1 -1 3 1
4
1 2 3 4
4
4 3 2 1
5
-1 -1 -1 -1 2
9
-1 -1 -1 -1 2 -1 -1 -1 3
11
-1 -1 -1 -1 2 -1 -1 -1 3 -1 -1
'''

    s += '{n}\n{ints}\n'.format(n=limit_n, ints=' '.join(['-1'] * limit_n))

    return io.StringIO(s)

def get_input(source):
    '''
    Generates a tuple with (N, [A1, ..., AN]) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            levels = list(map(int, next(lines).split(' ')))

            yield (n, levels,)

def calc(n, levels):
    # The chef starts at level 1.
    if levels[0] == -1:
        levels[0] = 1
    elif levels[0] != 1:
        return 0

    # Enforce validity and normalise trivial cases.
    prev = 1
    for i in range(len(levels), 0, -1):
        i -= 1
        level = levels[i]

        if prev != 1:
            expected = prev - 1

            if level == -1:
                level = expected
                levels[i] = expected
            elif level != expected:
                return 0

        prev = max(level, 1)

    if prev != 1:
        return 0

    # Now compute each case.
    solutions = 1
    blanks = 0
    for level in levels:
        if level != -1:
            if blanks != 0:
                solutions *= 2 ** blanks
                blanks = 0
        else:
            blanks += 1

    if blanks != 0:
        solutions *= 2 ** blanks

    return solutions % (10 ** 9 + 7)

if __name__ == '__main__':
    limit_n = 100000
    inp = test_data(limit_n) if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
