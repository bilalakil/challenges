#!/usr/bin/env python

# https://www.codechef.com/LTIME45/problems/COOMILK
# Passed.

import io
import sys

def test_data():
    '''
    Expected calculations:

    YES
    NO
    YES
    NO
    '''

    return io.StringIO(
'''4
7
cookie milk milk cookie milk cookie milk
5
cookie cookie milk milk milk
4
milk milk milk milk
1
cookie
'''
    )

def get_input(source):
    '''
    Generates a tuple containing a list of 'cookie' or 'milk' strings.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines).strip())
            foodstuffs = next(lines).strip().split(' ')[:n]

            yield (foodstuffs,)

def calc(foodstuffs):
    '''
    Returns a boolean.
    '''

    just_was_cookie = False

    for foodstuff in foodstuffs:
        if foodstuff == 'cookie':
            if just_was_cookie:
                return False

            just_was_cookie = True
        else:
            just_was_cookie = False

    return not just_was_cookie

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print('YES' if calc(*args) else 'NO')
