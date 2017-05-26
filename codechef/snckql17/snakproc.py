#!/usr/bin/env python

# https://www.codechef.com/SNCKQL17/problems/SNAKPROC
# Submission successful!

import io
import sys

def test_data():
    '''
    Expected answers:

    Valid
    Valid
    Invalid
    Valid
    Invalid
    Invalid
    '''

    return io.StringIO('''6
18
..H..T...HTH....T.
3
...
10
H..H..T..T
2
HT
11
.T...H..H.T
7
H..T..H''')

def get_input(source):
    '''
    Returns a tuple (R, report).
    '''

    with source as lines:
        t = int(next(lines))

        for _ in range(t):
            r = int(next(lines))
            report = next(lines).strip()

            yield (r, report,)

def snakejuice(r, report):
    expect = 'H'

    for c in report:
        if c == '.': continue
        if c != expect: return False
        expect = 'H' if expect == 'T' else 'T'

    return expect == 'H'

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print('Valid' if snakejuice(*args) else 'Invalid')

