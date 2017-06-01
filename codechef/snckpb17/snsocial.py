#!/usr/bin/env python
 
# https://www.codechef.com/SNCKQL17/problems/SNSOCIAL
# Submitted, but with non-zero exit code. Not sure why :(
# It was them! Worked all along.
 
import io
import sys
from itertools import product
 
def test_data():
    '''
    Expected answers:
 
    0
    1
    2
    4
    4
    4
    0
    499
    '''
 
    return io.StringIO('''8
2 2
1 1
1 1
2 2
1 1
1 2
3 4
1 2 1 2
1 1 1 2
1 1 2 2
8 8
1 1 1 1 1 5 1 1
1 5 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 5 1 1 1
9 1
2
1
1
1
1
1
1
1
2
1 9
1 1 1 1 9 1 1 1 1
500 500
''' + '\n'.join([' '.join(['1' for _ in range(500)]) for _ in range(500)]) + '''
500 500
''' + '\n'.join([' '.join(['100000'] + ['99999' for _ in range(499)])] + [' '.join(['99998' for _ in range(500)]) for _ in range(499)]))
 
def get_input(source):
    '''
    Returns a tuple (N, M, A).
    '''
 
    with source as lines:
        t = int(next(lines))
 
        for _ in range(t):
            n, m = map(int, next(lines).split(' '))
            a = [list(map(int, next(lines).split(' '))) for _ in range(n)]
 
            yield (n, m, a,)
 
# Will be used to loop around a square.
square_offsets = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
 
def calc(n, m, a):
    edges = set()
    max_ = 0
    time = 0
    
    for i, j in product(range(n), range(m)):
        v = a[i][j]
 
        if v > max_:
            max_ = v
            edges = set()
        if v == max_:
            edges.add((i, j,))

    remaining = set()

    for i, j in product(range(n), range(m)):
        if a[i][j] != max_:
            remaining.add((i, j,))

    while len(remaining) != 0:
        new_edges = set()
 
        for i, j in edges:
            for o_i, o_j in square_offsets:
                t = (i + o_i, j + o_j,)

                if t in remaining:
                    remaining.remove(t)
                    new_edges.add(t)
 
        edges = new_edges
        time += 1
 
    return time
 
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin
 
    for args in get_input(inp):
        print(calc(*args))
 
