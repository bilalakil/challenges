#!/usr/bin/env python

# https://www.codechef.com/COOK93A/problems/BINIM
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    Dum
    Dee
    '''

    return io.StringIO('''2
2 Dee
101
010
2 Dum
101
010''')

def get_input(source):
    '''
    Generates a tuple (N, P, S)
    where S is an array of strings.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, p = next(lines).strip().split(' ')
            n = int(n)

            s = [next(lines).strip() for _ in range(n)]

            yield (n, p, s)

def calc(n, p, s):
    '''
    Returns a string.
    '''

    counts = [0, 0]

    for stack in s:
        counts[int(stack[0])] += stack.count(stack[0])

    return 'Dee' if counts[0] > counts[1] or (counts[0] == counts[1] and p == 'Dum') else 'Dum'
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
       print(calc(*args))
