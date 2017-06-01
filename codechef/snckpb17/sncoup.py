#!/usr/bin/env python
 
# https://www.codechef.com/SNCKQL17/problems/SNCOUP
# Submitted successfully!
 
import io
import sys
 
def test_data():
    '''
    Expected answers:
 
    2
    3
    1
    5
    4
    9
    7
    8
    '''
 
    return io.StringIO('''8
2
**
**
3
***
*..
3
*..
.*.
10
.*.*.**..*
*..*..**..
10
.*.....*.*
*....*.*.*
10
*.*..*..**
***.******
10
*****.*.*.
**.*.*..*.
10
***.......
..**.***.*''')

def get_input(source):
    '''
    Returns a tuple (N, r1, r2) where r1 and r2 are strings.
    '''
 
    with source as lines:
        t = int(next(lines))
 
        for _ in range(t):
            n = int(next(lines))
            r1 = next(lines).strip()
            r2 = next(lines).strip()
 
            yield (n, r1, r2,)
 
def calc(n, r1, r2):
    r1_seen = False
    r2_seen = False
    r1_active = False
    r2_active = False
    fences = 0

    for i in range(n):
        drop_fence = False
        r1_on = r1[i] == '*'
        r2_on = r2[i] == '*'

        if r1_on:
            r1_seen = True

            if r1_active:
                drop_fence = True
                r2_active = r2_on
            else:
                r1_active = True

        if r2_on and not drop_fence:
            r2_seen = True

            if r2_active:
                drop_fence = True
                r1_active = r1_on
            else:
                r2_active = True

        if drop_fence:
            fences += 1

    return fences + (1 if r1_seen and r2_seen else 0)
 
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin
 
    for args in get_input(inp):
        print(calc(*args))
 
