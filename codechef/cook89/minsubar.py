#!/usr/bin/env python

# https://www.codechef.com/COOK89/problems/MINSUBAR
# Wrong, but not sure why.
# Asked for a failing test case here: https://discuss.codechef.com/questions/119992/minsubar-editorial/120171
import io
import sys

def test_data():
    '''
    Expected output:

    2
    1
    1
    '''

    return io.StringIO('''3
5 5
1 2 3 1 -5
5 1
1 2 3 1 -5
2 -100
-1000 -99''')

def get_input(source):
    '''
    Generates a tuple (N, A) for each test case.
    A is a list of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, d = map(int, next(lines).split(' '))
            a = list(map(int, next(lines).split(' ')[:n]))

            yield (n, d, a,)

def calc(n, d, a):
    '''
    Returns a number.
    '''

    _sum = a[0]
    count = 1

    if _sum >= d:
        return 1

    best = float('inf')
    combination_counts = [1] * n

    left = 0
    right = 0

    def inc_left(is_combine=False):
        nonlocal count
        nonlocal left
        nonlocal _sum

        if not is_combine:
            count -= combination_counts[left]
            _sum -= a[left]
        left += 1

    def inc_right():
        nonlocal count
        nonlocal right
        nonlocal _sum

        count += 1
        right += 1
        _sum += a[right]

    while True:
        if a[left] < 0:
            inc_left()
            inc_right()
        elif a[right] < 0:
            a[right] += a[left]
            combination_counts[right] += combination_counts[left]
            inc_left(True)

        if _sum < d:
            if right == len(a) - 1:
                break
            inc_right()
        else:
            if count < best:
                best = count
            if count == 1:
                break
            inc_left()

    return -1 if best == float('inf') else best
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
