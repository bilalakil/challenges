#!/usr/bin/env python

# https://www.codechef.com/COOK93A/problems/RUNDIR
# Found a counter-example too late (last test).
# Perhaps iterating backwards after flipping would work.
import io
import sys

def test_data():
    '''
    Expected output:

    0.5
    5
    -1
    -1
    -1
    0.6666666667
    '''

    return io.StringIO('''6
3
10 10
20 30
30 10
4
1 1
2 1000
10002 1000
10003 1
5
1 10
2 9
3 8
4 7
5 10
1
1 1
2
1 1
2 2
5
10 10
20 20
40 10
50 24
60 5''')

def get_input(source):
    '''
    Generates a tuple (N, S)
    where S is an array of tuples (X, V).
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))

            s = []
            for _ in range(n):
                s.append(tuple(map(int, next(lines).split(' '))))

            yield (n, s)

def calc(n, s):
    '''
    Returns an integer.
    '''

    s = sorted(s, key=lambda _: _[0])

    min_max = float('inf')

    prev_d = -1

    for i in range(1, len(s) - 1):
        cur = s[i]

        times = []

        for d in [-1, 1]:
            o = s[i + d]
            o_d = prev_d if d == -1 else 1

            if o_d == d and cur[1] <= o[1]:
                prev_d = d
                break

            times.append(abs((cur[0] - o[0]) / (cur[1] + o[1] * o_d)))

        if len(times) != 2:
            continue

        if times[0] >= times[1]:
            prev_d = -1
            time = times[0]
        else:
            time = times[1]

        min_max = min(min_max, time)

    return -1 if min_max == float('inf') else min_max
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
       print(calc(*args))
