#!/usr/bin/env python

# https://www.codechef.com/COOK83/problems/ADACRA
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    1
    0
    0
    2
    '''

    return io.StringIO('''4
UUDDDUUU
UUUUU
DDDDD
UDUDU''')

def get_input(source):
    '''
    Generates a tuple (S) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            s = next(lines).strip()

            yield (s,)

def calc(s):
    '''
    Returns an integer.
    '''

    chars = set(['U', 'D'])
    grps = {l: 0 for l in chars}
    cur = ''

    for l in s:
        if l not in chars or l == cur: continue

        cur = l
        grps[l] += 1

    return min(grps.values())
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
