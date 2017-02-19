#!/usr/bin/env python

# https://www.codechef.com/COOK79/problems/CHAIRS
# Solution successful!
import io
import sys

def test_data():
    '''
    Expected output:

    2
    4
    7
    '''

    return io.StringIO('''3
8
10001010
11
10010001001
15
00010010001001
''')

def get_input(source):
    '''
    Generates a tuple with a single string for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            chairs = next(lines).strip()

            yield (chairs,)

def calc(chairs):
    # Shift the starting zeroes to the end, so we start with a '1'.
    tmp_chairs = chairs.lstrip('0')
    chairs = tmp_chairs + '0' * (len(chairs) - len(tmp_chairs))

    # Remove any 1s from the end (if there were no starting zeroes) -
    # they make no difference.
    chairs = chairs.rstrip('1')

    empties = 0
    distances = []

    for chair in chairs:
        if chair == '1':
            if empties != 0:
                distances.append(empties)
                empties = 0
        else:
            empties += 1

    if empties != 0:
        distances.append(empties)

    return sum(sorted(distances)[:-1])

# This failed submission was due to a misunderstanding:
# I thought the child rotates to the last available chair in a particular direction,
# as opposed to the first...
def calc_derp(chairs):
    first = chairs[0]
    prev = first
    movements = 0

    for chair in chairs[1:]:
        if prev == chair:
            continue
        elif chair == '1':
            movements += 1

        prev = chair

    if first == prev and first == '1':
        movements = max(movements - 1, 0)
        
    return movements

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
