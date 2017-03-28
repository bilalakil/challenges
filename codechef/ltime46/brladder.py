#!/usr/bin/env python

# https://www.codechef.com/COOK80/problems/BRLADDER
# Stuffed up the timezones (and alarm) - 1:15 after the competition ended.
# Solved here: https://www.codechef.com/problems/BRLADDER
import io
import sys

def test_data():
    '''
    Expected output:

    NO
    YES
    NO
    YES
    YES
    YES
    NO
    '''

    return io.StringIO('''7
1 4
4 3
5 4
10 12
1 3
999999999 1000000000
17 2384823''')

def get_input(source):
    '''
    Generates a tuple (a, b) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            a, b = list(map(int, next(lines).strip().split(' ')))

            yield (a, b,)

def calc(a, b):
    '''
    Returns a boolean.
    '''

    l = min(a, b)
    u = max(a, b)

    return (u % 2 == 0 and l + 1 == u) or l + 2 == u

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print('YES' if calc(*args) else 'NO')
