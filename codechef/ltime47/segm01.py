#!/usr/bin/env python

# https://www.codechef.com/LTIME47/problems/SEGM01
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    YES
    NO
    NO
    YES
    NO
    NO
    '''

    return io.StringIO('''6
001111110
00110011
000
1111
101010101
101111111111''')

def get_input(source):
    '''
    Generates a tuple (S,) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            s = next(lines).strip()

            yield (s,)

def calc(s):
    '''
    Returns a boolean.
    '''

    has_1 = False

    for l in s.strip('0'):
        if l == '1':
            has_1 = True

        if l == '0' and has_1:
            return False

    return has_1

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print('YES' if calc(*args) else 'NO')
