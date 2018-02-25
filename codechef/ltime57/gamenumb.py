#!/usr/bin/env python

# https://www.codechef.com/LTIME57/problems/GAMENUMB
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    7
    '''

    return io.StringIO('''1
4 2
1 2 3 4
2 2 2 2
6 3''')

def get_input(source):
    '''
    Generates a tuple (N, K, A, D, B) for each test case,
    where A, D and B are lists of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, k = map(int, next(lines).strip().split(' '))
            a = list(map(int, next(lines).strip().split(' ')[:n]))
            d = list(map(int, next(lines).strip().split(' ')[:n]))
            b = list(map(int, next(lines).strip().split(' ')[:k]))

            yield (n, k, a, d, b,)

def calc(n, k, a, d, b):
    '''
    Returns an integer.
    '''

    fr = 1
    to = sum(d)

    for i, num in enumerate(b):
        if i % 2 == 0: fr = to - num + 1
        else:          to = fr + num - 1
    
    ind = []
    for i in range(n):
        ind.append({ 'a': a[i], 'd': d[i] })

    ind = sorted(ind, key=lambda i: i['a'])

    cur = 1
    for i in range(n):
        ind[i]['fr'] = cur
        ind[i]['to'] = cur + ind[i]['d'] - 1

        if fr >= ind[i]['fr'] and fr <= ind[i]['to']: ind_fr = i
        if to >= ind[i]['fr'] and to <= ind[i]['to']: ind_to = i

        cur = ind[i]['to'] + 1

    total = 0
    for i in range(ind_fr, ind_to + 1):
        total += ind[i]['a'] * (min(ind[i]['to'], to) - max(ind[i]['fr'], fr) + 1)

    return total

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
