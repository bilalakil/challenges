#!/usr/bin/env python

# https://www.codechef.com/COOK88/problems/SKIING
# Currently incorrect on the second-last test-case, for obvious reasons.
# Haven't fixed because I'm looking for the cause of a crash, which I cannot find ;(
# That crash is only happening on submit - not on these test cases.
#
# I've asked for help here: https://discuss.codechef.com/questions/118024/skiing-editorial/118122
import io
import sys

max_n = 1000
max_m = 1000
max_h = 10 ** 9

def test_data():
    '''
    Expected output:

    2
    1
    3
    2
    5
    1
    '''

    return io.StringIO('''6
3 3
1 2 2
2 1 1
2 1 1
3 3
3 2 2
2 1 1
2 1 1
3 2
7 1
1 7
7 1
3 2
7 7
1 7
7 1
3 3
7 5 7
5 6 5
7 5 7
{} {}
{}'''.format(max_n, max_m, '\n'.join([' '.join([str(max_h) for _ in range(max_m)]) for _ in range(max_n)])))

def get_input(source):
    '''
    Generates a tuple (N, M, G) for each test case.
    G is a two-dimentional list (of size N * M) of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            g = []
            n, m = list(map(int, next(lines).split(' ')))

            for _ in range(n):
                c = list(map(int, next(lines).split(' ')))
                g.append(c)

            yield (n, m, g)

def calc(n, m, g):
    '''
    Returns an integer.
    '''

    cur_max = 0
    maxes = set()

    for i in range(n):
        for j in range(m):
            h = g[i][j]
            p = (i, j,)

            if h > cur_max:
                cur_max = h
                maxes = set()

            if h == cur_max:
                maxes.add(p)

    branches = 0
    to_visit = set()
    visited = set()

    while len(maxes) > 0:
        branches += 1

        mak = maxes.pop()
        to_visit.add(mak)
        visited.add(mak)

        while len(to_visit) > 0:
            cur = to_visit.pop()
            i, j = cur

            if cur in maxes: maxes.remove(cur)

            for di, dj in [(-1, 0,), (0, -1,), (1, 0,), (0, 1,)]:
                ni = i + di
                nj = j + dj
                new = (ni, nj,)

                if (
                    new in visited or
                    ni < 0 or ni == n or
                    nj < 0 or nj == m or
                    g[ni][nj] > g[i][j]
                ):
                    continue

                to_visit.add(new)
                visited.add(new)

    return branches
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
