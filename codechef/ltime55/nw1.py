#!/usr/bin/env python

# https://www.codechef.com/LTIME55/problems/NW1
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    4 4 4 4 4 4 4
    4 4 5 5 5 4 4
    5 4 4 4 4 4 5
    '''

    return io.StringIO('''3
28 mon
31 wed
30 sun''')

def get_input(source):
    '''
    Generates a tuple (W, D) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            w, d = next(lines).strip().split(' ')
            w = int(w)

            yield (w, d,)

def calc(w, d):
    '''
    Returns a list of seven integers.
    '''

    day_names = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
    days = [4]*7

    for i in range(w-28):
        days[(day_names.index(d) + i) % 7] += 1

    return days

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(' '.join(map(str, calc(*args))))
