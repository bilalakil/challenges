#!/usr/bin/env python

# https://www.codechef.com/COOK89/problems/FBMT
# Submission successful!
import io
import sys

def test_data():
    '''
    Expected output:

    Draw
    yyy
    '''

    return io.StringIO('''2
4
ab
bc
bc
ab
3
xxx
yyy
yyy''')

def get_input(source):
    '''
    Generates a tuple (N, S) for each test case.
    S is a list of strings.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            s = list(map(lambda _: next(lines).strip(), range(n)))

            yield (n, s)

def calc(n, s):
    '''
    Returns a string.
    '''

    first = None
    second = None
    fscore = 0
    sscore = 0

    for team in s:
        if first == None:
            first = team
        elif second == None and team != first:
            second = team

        if team == first:
            fscore += 1
        else:
            sscore += 1

    return 'Draw' if fscore == sscore else (first if fscore > sscore else second)
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
