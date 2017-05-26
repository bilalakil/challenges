#!/usr/bin/env python

# https://www.codechef.com/SNCKQL17/problems/SNAKEEAT
# Not submitted; the real problem wasn't solved :P

import io
import sys

def test_data():
    '''
    Expected answers:

    3
    1
    0
    '''

    return io.StringIO('''2
5 2
21 9 5 8 10
10
15
5 1
1 2 3 4 5
100''')

def get_input(source):
    '''
    Returns a tuple (N, Q, [L1, L2, ..., Ln], [K1, K2, ..., Kn]).
    '''

    with source as lines:
        t = int(next(lines))

        for _ in range(t):
            n, q = map(int, next(lines).split(' '))
            snakes = list(map(int, next(lines).strip().split(' ')))
            queries = [int(next(lines)) for _ in range(q)]

            yield (n, q, snakes, queries,)

# Naive: efficient for a single query, but not 10,000 of them.
def bear_limak_is_back(n, q, snakes, queries):
    snakes = sorted(snakes, reverse=True)
    
    query_results = []
    for k in queries:
        i = -1
        j = 0

        while i != n - 1:
            i += 1
            l = snakes[i]

            if l >= k: continue

            deficit = k - l

            if n - 1 - i - j < deficit:
                i -= 1
                break

            j += deficit

        query_results.append(i + 1)

    return query_results

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        for o in bear_limak_is_back(*args): print(o)

