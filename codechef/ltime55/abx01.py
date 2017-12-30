#!/usr/bin/env python

# https://www.codechef.com/LTIME55/problems/ABX01
# I found power digital root but somehow was still wrong (see the last test).
# I suppose it's a precision issue, but I couldn't find it for the life of me :(...
# I tried using a string sum instead of a modulo thingo for the normal digital root, to no avail.
import io
import math
import sys

def test_data():
    '''
    Expected output:

    7
    4
    1
    1
    1
    7
    9
    1
    2
    1
    '''

    return io.StringIO('''10
5 2
7 2
127 1
10000 100
1000000000000000000 1000000000000000000
4740317473395506 474536
1332951641590611 752071
4255560267055840 507550
417487876351088 270239
9384523984751983475198234571 189237415924512349''')

def get_input(source):
    '''
    Generates a tuple (A, N) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            a, n = map(int, next(lines).split(' '))

            yield (a, n,)

def calc(a, n):
    '''
    Returns an integer.
    '''

    # Digital Root FTW! http://people.revoledu.com/kardi/tutorial/DigitSum/Digital-Power.html
    def dr(x):
        return 1 + (x-1) % 9
    def pdr(x, y):
        drx = dr(x)

        ans = 1
        for _ in range(y - 6 * int((y - 2) / 6)):
            ans = dr(ans * drx)

        return ans

    return pdr(a, n)

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
