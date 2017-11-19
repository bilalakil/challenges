#!/usr/bin/env python

# https://www.codechef.com/COOK88/problems/ONCHESS
# Successfully submitted!
import io
import sys

def test_data():
    '''
    Expected output:

    wait
    wait
    1
    2
    wait
    wait
    5
    '''

    return io.StringIO('''1
7
5 1 10 15 rated random
11 1 20 15 rated random
10 3 30 15 rated random
2 5 15 15 rated random
30 20 60 60 unrated white
50 20 40 60 unrated random
50 20 40 60 unrated black''')

def get_input(source):
    '''
    Generates a tuple (N, P) for each test case.
    P is a list of player data in the form (R, Mi, Ma, T, Ranked, Colour).
    R, Mi, Ma and T are integers. Ranked and Colour are strings.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            p = []
            n = int(next(lines))

            for _ in range(n):
                r, mi, ma, t, ranked, colour = next(lines).strip().split(' ')
                p.append((int(r), int(mi), int(ma), int(t), ranked, colour,))

            yield (n, p)

def calc(n, p):
    '''
    Returns a list of strings.
    '''

    waiting = []

    for i, person in enumerate(p):
        found = False

        for pos_j, j in enumerate(waiting):
            other = p[j]

            if (
                other[1] <= person[0] and person[0] <= other[2] and
                person[1] <= other[0] and other[0] <= person[2] and
                other[3] == person[3] and
                other[4] == person[4] and
                (
                    (other[5] == 'black' and person[5] == 'white') or
                    (other[5] == 'white' and person[5] == 'black') or
                    (other[5] == 'random' and person[5] == 'random')
                )
            ):
                yield j + 1

                del waiting[pos_j]
                found = True
                break

        if not found:
            yield 'wait'
            waiting.append(i)
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        for state in calc(*args):
            print(state)
