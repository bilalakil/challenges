#!/usr/bin/env python

# https://www.codechef.com/COOK83/problems/CENTREE
# Wrong answer.
#
# Submitted without the n < 3 check, which is necessary as described
# [here](https://discuss.codechef.com/questions/102384/can-anybody-find-my-mistake/102385).
# However I don't understand why it's necessary (according to the constraints),
# and even so, the answer was still wrong.
#
# Asked for an example contradiction [here](https://discuss.codechef.com/questions/102434/).
# Now correct after the feedback from that question,
# which I'm honestly still confused by.
#
# I asked for more explanation [here](https://discuss.codechef.com/questions/102432/centree-editorial/102563),
# and the nail was finally hit on the head -
# I didn't consider the _maximum_ distance, but rather any distance.
import io
import sys

def test_data():
    '''
    Expected output:

    YES
    1 2
    1 3
    1 4
    NO
    YES
    1 2
    '''

    return io.StringIO('''3
4 0
2 0
2 1''')

def get_input(source):
    '''
    Generates a tuple (N, B) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, b = map(int, next(lines).split(' '))

            yield (n, b,)

def calc(n, b):
    '''
    Returns None or a list of tuples (u, v).
    '''

    if n == 2 and b == 1:
        return [(1, 2,)]
    if n < 3 or b != 0 and n / b < 4:
        return None

    edges = []

    broom_length = b * 2 + 1
    for i in range(1, n):
        i += 1

        edges.append((i, i + 1 if i < broom_length else 1,))

    return edges
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        edges = calc(*args)

        if edges == None:
            print('NO')
        else:
            print('YES')
            for e in edges:
                print('{} {}'.format(*e))

