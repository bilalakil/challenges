#!/usr/bin/env python

# https://www.codechef.com/COOK83/problems/SNACKUP
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    2
    2
    1 1 2
    2 2 1
    2
    1 2 1
    2 1 2
    3
    3
    1 1 2
    2 2 3
    3 3 1
    3
    1 2 3
    2 3 1
    3 1 2
    3
    1 3 1
    2 1 2
    3 2 3
    '''

    return io.StringIO('''2
2
3''')

def get_input(source):
    '''
    Generates a tuple (N) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))

            yield (n,)

def calc(n):
    '''
    Returns a list of lists of tuples:
    
    ```
    [
        [
            (1, 1, 2),
            (2, 1, 2)
        ],
        [
            (1, 1, 2),
            (2, 1, 2)
        ]
    ]
    ```
    
    r is the length of the outer list.
    k is the length of the inner list (in each round).
    '''

    rounds = []

    for i in range(n):
        rounds.append([])
        r = rounds[i]
        for j in range(n):
            r.append((j + 1, (j + i) % n + 1, (j + i + 1) % n + 1,))

    return rounds
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        rounds = calc(*args)

        print(len(rounds))
        for r in rounds:
            print(len(r))
            for judge in r:
                print('{} {} {}'.format(*judge))
