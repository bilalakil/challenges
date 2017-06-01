#!/usr/bin/env python
 
# https://www.codechef.com/SNCKQL17/problems/SNDISCUS
# Submitted but incorrect :P
#
# No idea why incorrect. Asked here: https://discuss.codechef.com/questions/99970/sndiscus-editorial/100054
 
import io
import sys
import math
 
def test_data():
    '''
    Expected answers:
 
    0
    1
    1
    5
    0
    0
    49
    49
    49
    25
    3
    '''
 
    return io.StringIO('''11
2
1 1 1 3
1 1 3 1
2
1 1 1 3
2 1 3 1
3
1 1 1 3
2 1 3 1
2 2 2 2
9
8 6 0 6
2 4 2 6
0 3 6 3
2 7 2 2
5 8 9 8
2 3 2 3
5 8 5 4
6 6 6 5
9 5 9 6
1
50 50 1 50
2
50 50 50 50
50 50 50 50
2
50 50 50 50
1 1 1 1
3
50 50 50 50
1 1 1 1
50 1 50 1
4
50 50 50 50
50 1 50 1
1 1 1 1
1 50 1 50
2
50 50 50 50
50 1 50 1
5
6 1 6 1
7 2 7 2
8 4 8 4
6 6 6 6
5 5 5 5''')

def get_input(source):
    '''
    Returns a tuple (N, snakes) where snakes is an array of tuples ((x1, y1), (x2, y2)).
    '''
 
    with source as lines:
        t = int(next(lines))
 
        for _ in range(t):
            n = int(next(lines))
            snakes = [list(map(int, next(lines).split(' '))) for _ in range(n)]
            snakes = [((s[0], s[1],), (s[2], s[3],),) for s in snakes]
 
            yield (n, snakes,)
 
def pointsnake(n, snakes):
    max_dist = 0

    def comp_points(sn1, sn2, axis):
        axis = 0 if axis == 'x' else 1

        s1 = min(sn1[0][axis], sn1[1][axis])
        l1 = max(sn1[0][axis], sn1[1][axis])
        s2 = min(sn2[0][axis], sn2[1][axis])
        l2 = max(sn2[0][axis], sn2[1][axis])

        if (s2 >= s1 and s2 <= l1) or (l2 >= s1 and l2 <= l1):
            return (0, 0,)
        elif l2 < s1:
            return (s1, l2,)

        return (l1, s2,)

    def compare_snakes(sn1, sn2):
        nonlocal max_dist

        x1, x2 = comp_points(sn1, sn2, 'x')
        y1, y2 = comp_points(sn1, sn2, 'y')

        max_dist = max(max_dist, abs(x1 - x2) + abs(y1 - y2))

    for i in range(n):
        for j in range(i, n):
            if i == j: continue

            compare_snakes(snakes[i], snakes[j])

    return math.ceil(max_dist / 2)
 
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin
 
    for args in get_input(inp):
        print(pointsnake(*args))
 
