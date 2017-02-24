#!/usr/bin/env python

# https://www.codechef.com/COOK78/problems/LISDIGIT
# Submission successful!
import io
import sys

def test_data():
    '''
    Example output (NB: there is more than one correct answer):

    7
    36
    54
    1531
    1730418
    '''

    return io.StringIO('''5
1 
1
2 
1 2
2 
1 1
4
1 2 2 1
7 
1 2 2 1 3 2 4
''')

def get_input(source):
    '''
    Generates a tuple (K, A), where K is an integer and A is a tuple of integers.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            lis_arr = list(map(int, next(lines).split(' ')))

            yield (n, lis_arr,)

def calc(n, lis_arr):
    return calc_insertion(n, lis_arr)

def calc_insertion(n, lis_arr):
    first_digit_with_lis = { 0: -1 }
    digit_order = [-1]

    for i in range(len(lis_arr)):
        lis = lis_arr[i]

        if lis not in first_digit_with_lis:
            first_digit_with_lis[lis] = i

        prev_digit = first_digit_with_lis[lis - 1]
        prev_digit_index = digit_order.index(prev_digit)
        digit_order.insert(prev_digit_index, i)

    digits = list(map(str, range(1, 10)))
    val = ' ' * n

    for d in digit_order[:-1]:
        val = val[0:d] + digits.pop() + val[d+1:]

    return int(val)

# Discovered this much simpler solution whilst working on the followup question.
# Just turn the LIS array itself into an integer...
#
# Would need to be extended slightly to handle zeroes if `n > 9`,
# but this problem was constrained such that that isn't necessary.
#
# Note that this solution is not the one that was submitted.
def calc_derp(n, lis_arr):
    return int(''.join(list(map(str, lis_arr))))

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    f = calc
    if '-1' in sys.argv:
        f = calc_insertion
    elif '-2' in sys.argv:
        f = calc_derp

    for args in get_input(inp):
        print(f(*args))
