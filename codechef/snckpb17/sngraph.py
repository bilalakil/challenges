#!/usr/bin/env python
 
# https://www.codechef.com/SNCKQL17/problems/SNGRAPH
# Submitted a simple test, which didn't work :P Found a contradiction at least.
 
import io
import sys
 
def test_data():
    '''
    Expected answers:
 
    0 3 4 4 4
    0
    2 3 5 5 5 5
    0 0 0 0 0 5
    0 0 2 8 8 8 8 8 8
    '''
 
    return io.StringIO('''5
5 4
1 2
2 3
2 4
4 5
1 0
6 4
2 6
3 4
3 6
4 6
6 15
1 2
1 3
1 4
1 5
1 6
2 3
2 4
2 5
2 6
3 4
3 5
3 6
4 5
4 6
5 6
9 14
1 2
1 3
2 4
2 5
2 6
4 5
4 6
5 6
3 7
3 8
3 9
7 8
7 9
8 9''')

def get_input(source):
    '''
    Returns a tuple (N, M, edges) where edges is a tuple of (u, v).
    '''
 
    with source as lines:
        t = int(next(lines))
 
        for _ in range(t):
            n, m = map(int, next(lines).split(' '))
            edges = [tuple(map(int, next(lines).split(' '))) for _ in range(m)]
 
            yield (n, m, edges,)
 
def calc(n, m, edges):
    if n == 1:
        return [0]

    counts = []
    degrees = [0] * n

    for i, j in edges:
        degrees[i - 1] += 1
        degrees[j - 1] += 1

    degrees = sorted(degrees)
    cursor = 0

    for i in range(n):
        while cursor < n - 1 and degrees[cursor] <= i:
            cursor += 1

        counts.append(cursor)

    return counts
 
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin
 
    for args in get_input(inp):
        print(' '.join(map(str, calc(*args))))
 
