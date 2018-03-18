#!/usr/bin/env python

# https://www.codechef.com/COOK92A/problems/CO92MATR
# Submitted successfully!
import io
import sys

def test_data():
    '''
    Expected output:

    1 2 2 3
    1 7 7 100
    6 10 20 101
    7 11 21 20000
    -1
    '''

    return io.StringIO('''2
4 4
1 2 2 3
1 -1 7 -1
6 -1 -1 -1
-1 -1 -1 -1
2 3
1 4 -1
1 -1 3''')

def get_input(source):
    '''
    Generates a tuple (N, M, matrix) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, m = map(int, next(lines).split(' '))
            matrix = []

            for _ in range(n):
                matrix.append(list(map(int, next(lines).split(' ')[:m])))

            yield (n, m, matrix)

def calc(n, m, matrix):
    '''
    Returns a matrix or -1.
    '''

    for i in range(n):
        for j in range(m):
            prev_row = matrix[i - 1][j] if i - 1 != -1 else 0
            prev_col = matrix[i][j - 1] if j - 1 != -1 else 0
            prev = max(prev_row, prev_col)

            if matrix[i][j] == -1:
                matrix[i][j] = max(prev, 1)
            else:
                if matrix[i][j] < prev:
                    return -1

    return matrix
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        val = calc(*args)

        if val == -1:
            print(val)
        else:
            for row in calc(*args):
                print(' '.join(map(str, row)))
