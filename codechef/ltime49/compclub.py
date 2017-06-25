#!/usr/bin/env python

# https://www.codechef.com/LTIME49/problems/COMPCLUB
# Submitted for 0.2, with NZEC on larger inputs.
# I realised a recursion depth limit exception; not sure if there's something else.
#
# Tried submitting a non-recursive solution (to practice), which got the same 0.2,
# but otherwise opened a whole new can of worms (wrong answer, too long).
import io
import sys
from itertools import zip_longest

def test_data():
    '''
    Expected output:

    4
    2
    2
    1
    1
    12
    6
    2
    3
    1
    2
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    2
    4
    0
    0
    1
    2
    3
    1
    0
    0
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    0
    0
    1
    1
    1
    0
    1
    1
    1
    1
    1
    1
    1
    1
    0
    1'''

    return io.StringIO('''5
5 3
0 1 2 3
0 0 0 0 0
2 1 1 0 0
15 3
0 1 1 2 3 3 4 5 5 6 7 8 9 10
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3 2 1 2 0 2 2 1 1 1 1 0 0 0 0
36 5
0 0 1 1 1 2 2 3 3 4 4 5 6 7 7 7 8 8 9 10 11 12 13 14 15 16 16 18 19 25 26 28 29 30 31
0 0 1 2 0 0 1 2 2 0 0 0 1 1 4 3 2 2 2 0 0 2 1 2 3 2 1 0 2 0 2 2 2 0 0 1
5 4 2 2 4 4 1 2 1 3 3 1 0 0 0 0 1 0 0 2 0 0 1 2 0 1 1 1 1 1 0 0 0 0 0 0
1 1
0
1
1 0

0
0''')

# Nice tree creation function [from SO](https://codereview.stackexchange.com/a/71278/131994).
def tree(edges):
    tree = {}

    for e, u in enumerate(edges):
        v = e + 1
        tree.setdefault(u, {}).setdefault('n', []).append(v)
        tree.setdefault(v, {})['p'] = u

    return tree

def get_input(source):
    '''
    Generates a tuple (N, X, T, V) for each test case,
    where T is a tree dictionary,
    and V is a list of vertex properties (C, K).
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, x = map(int, next(lines).split(' '))

            nl = next(lines).strip()
            if n == 1:
                t = {}

                if nl == '':
                    nl = next(lines).strip()
            else:
                t = tree(map(int, nl.split(' ')))
                nl = next(lines).strip()

            v = list(zip(list(map(int, nl.split(' '))), list(map(int, next(lines).split(' ')))))

            yield (n, x, t, v)

def merge(branches):
    if len(branches) == 0:
        return {}
    if len(branches) == 1:
        return branches[0]

    res = {}
    clubs = set().union(*[b.keys() for b in branches])

    for c in clubs:
        bs = [b[c] for b in branches if c in b]

        if len(bs) == 0:
            break

        res[c] = list(map(sum, list(zip_longest(*bs, fillvalue=0))))

    return res

def calc(n, x, t, v):
    '''
    Returns a list of integers.
    '''

    counts = [0] * n

    visited = set()
    i = 0

    while i != None:
        if i in t:
            if 'n' in t[i] and len(t[i]['n']) > 0:
                i = t[i]['n'].pop()
                continue

        if i not in visited:
            c, k = v[i]

            if i in t and 'b' in t[i]:
                branch = merge(t[i]['b'])
            else:
                branch = {}

            if k == 0:
                if c not in branch:
                    branch[c] = [0]

                branch[c][0] += 1
                counts[i] = 1
            elif c in branch and len(branch[c]) >= k:
                if len(branch[c]) == k:
                    branch[c].append(0)

                prev = branch[c][k - 1]
                counts[i] = prev
                branch[c][k] += prev

            visited.add(i)

        if i in t:
            if 'b' in t[i]:
                del t[i]['b']

            i = t[i]['p'] if 'p' in t[i] else None

            if i != None:
                t[i].setdefault('b', []).append(branch)
        else:
            i = None

    return counts

def calc_recursive(n, x, t, v):
    '''
    Returns a list of integers.
    '''

    counts = [0] * n

    def dfs(i):
        c, k = v[i]

        if i not in t or 'n' not in t[i]:
            if k == 0:
                counts[i] = 1
                return { c: [1] }
            return {}

        branch = merge([dfs(j) for j in t[i]['n']])

        if k == 0:
            if c not in branch:
                branch[c] = [1]
            else:
                branch[c][0] += 1

            counts[i] = 1
        elif c in branch and len(branch[c]) >= k:
            if len(branch[c]) == k:
                branch[c].append(0)

            prev = branch[c][k - 1]
            counts[i] = prev
            branch[c][k] += prev

        return branch

    dfs(0)

    return counts

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    f = calc
    if '-1' in sys.argv:
        f = calc_recursive

    for args in get_input(inp):
        for n in f(*args):
            print(n)
