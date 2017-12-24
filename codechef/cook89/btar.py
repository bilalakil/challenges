#!/usr/bin/env python

# https://www.codechef.com/COOK89/problems/BTAR
# Submission successful!
import io
import sys

def test_data():
    '''
    Expected output:

    3
    '''

    return io.StringIO('''1
7
1 2 3 1 2 3 8''')

def get_input(source):
    '''
    Generates a tuple (N, A) for each test case.
    A is a list of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            a = list(map(int, next(lines).split(' ')[:n]))

            yield (n, a,)

def calc(n, a):
    '''
    Returns a number.
    '''

    modcounts = {1: 0, 2: 0, 3: 0}

    for num in a:
        mod = num % 4

        if mod != 0:
            modcounts[mod] += 1

    if (modcounts[1] + modcounts[2]*2 + modcounts[3]*3) % 4 != 0:
        return -1

    steps = 0

    steps += modcounts[2] // 2
    modcounts[2] = modcounts[2] % 2

    num1s3s = min(modcounts[1], modcounts[3])
    steps += num1s3s
    modcounts[1] -= num1s3s
    modcounts[3] -= num1s3s

    remaining = modcounts[1] if modcounts[1] != 0 else modcounts[3]

    if modcounts[2] == 1:
        steps += 2
        remaining -= 2
    
    steps += (remaining // 4) * 3

    return steps
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
