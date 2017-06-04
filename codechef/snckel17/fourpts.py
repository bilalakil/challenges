#!/usr/bin/env python
 
# https://www.codechef.com/SNCKEL17/problems/FOURPTS
# Submitted, but wrong ;(
 
import io
import sys
import math
 
def test_data():
    '''
    Expected answers:
 
    YES 1 3 2 1 1 1.0
    YES 2 2 2 0 0.0 0.0
    NO
    YES 0 0 4 0 0 4.0
    YES 0 0 4 4 4 0.0
    NO
    NO
    YES 4 5 7 5 5 5
    YES 4 5 4 8 4 6
    YES 4 5 9 9 6.0 5.0
    YES 4 5 9 9 4 7.0
    YES -50 -40 -45 -50 -40.0 -40.0
    YES 0 10 -20 -20 0 -10.0
    YES 20 20 20 -20 20 0
    YES 0 0 7 0 3.5 3.5
    YES -4 2 14 -34 6.0 4.0
    YES 29 33 19 12 46.5 -4.5
    YES 49 12 19 12 45.8421052631579 21.473684210526315
    YES 29 33 29 6 52.82352941176472 13.147058823529415
    YES 100 100 100 -300 -300.0 100.0
    '''
 
    return io.StringIO('''20
1 1 1 3 1 2 2 1
1 1 2 2 2 0 1 0
0 0 10 0 0 10 1 1
0 0 2 0 0 2 2 2
0 0 2 2 4 2 2 0
0 0 4 5 10 0 5 1
0 0 2 3 6 1 2 2
4 5 5 5 6 5 7 5
4 5 4 6 4 7 4 8
4 5 5 5 6 5 9 9
4 5 4 6 4 7 9 9
-50 -40 -45 -40 -40 -40 -45 -50
0 0 0 10 0 -10 -20 -20
20 20 20 0 20 -5 20 -20
0 0 7 0 2 2 6 1
-4 2 1 3 10 -15 5 -16
29 33 36 18 29 6 19 12
36 18 47 18 49 12 19 12
29 33 47 18 49 12 29 6
100 100 100 -100 -100 -100 -100 100''')

def get_input(source):
    '''
    Returns a tuple (p1, p2, p3, p4) where each point is a tuple of integers (x, y).
    '''
 
    with source as lines:
        t = int(next(lines))
 
        for _ in range(t):
            p = list(map(int, next(lines).split(' ')))
            yield list(((p[0], p[1],), (p[2], p[3],), (p[4], p[5],), (p[6], p[7],),))

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Inside triangle formula from: https://stackoverflow.com/a/2049593/1406230
def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1]) < 0

def is_inside_triangle(pt, tri):
    s1 = sign(pt, tri[0], tri[1])
    s2 = sign(pt, tri[1], tri[2])
    s3 = sign(pt, tri[2], tri[0])

    return s1 == s2 and s2 == s3

def line_from_points(p1, p2):
    ''' Returns a tuple (m, c) to be used in the formula y = mx + c. '''
    if p1[0] == p2[0]:
        return {'x-only': True, 'c': p1[0]}

    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return {'x-only': False, 'm': m, 'c': p1[1] - m * p1[0]}

def create_triangle(farthest, other):
    angle = -1
    largest_i = -1
    for i in [0, 1]:
        p = other[i]

        a = dist(farthest[0], farthest[1])
        b = dist(farthest[0], p)
        c = dist(farthest[1], p)

        theta = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))

        if theta > angle:
            angle = theta
            largest_i = i

    l1 = line_from_points(farthest[1], other[largest_i])
    l2 = line_from_points(farthest[0], other[abs(largest_i - 1)])
    
    x = None
    y = None

    if l1['x-only'] and l2['x-only']:
        if l1['c'] != l2['c']:
            return None
        
        x, y = other[0]
    elif l1['x-only'] or l2['x-only']:
        s = l1 if l1['x-only'] else l2
        o = l2 if l1['x-only'] else l1

        x = s['c']
        y = x * o['m'] + o['c']
    elif l1['m'] == l2['m']:
        if l1['c'] == l2['c']:
            x, y = other[0]
        else:
            return None
    else:
        x = (l1['c'] - l2['c']) / (l2['m'] - l1['m'])
        y = l1['m'] * x + l1['c']

    return (farthest[0], farthest[1], (x, y,),)

def calc(pts):
    max_dist = -1
    farthest = None
    other = None

    for i in range(4):
        if is_inside_triangle(pts[i], pts[0:i] + pts[i + 1:]):
            xs = sum(1 if pts[i][0] == o[0] else 0 for o in pts[0:i] + pts[i + 1:])
            ys = sum(1 if pts[i][1] == o[1] else 0 for o in pts[0:i] + pts[i + 1:])

            if xs < 2 and ys < 2:
                return None

        for j in range(i, 4):
            pi = pts[i]
            pj = pts[j]

            d = dist(pi, pj)
            if d > max_dist:
                tmp_other = tuple(map(lambda k: pts[k], set(range(4)) - set([i, j])))

                # Don't take it if it splits the other points on either side of the line.
                signs = [sign(o, pi, pj) for o in tmp_other]
                if signs[0] != signs[1]:
                    continue

                max_dist = d
                farthest = (pi, pj,)
                other = tmp_other

    tri = create_triangle(farthest, other)

    # Parallelogram; extend one point outwards and try again.
    if tri == None:
        farthest = (farthest[0], (farthest[1][0] * 2 - farthest[0][0], farthest[1][1] * 2 - farthest[0][1],),)
        tri = create_triangle(farthest, other)

    return tri
 
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin
 
    for points in get_input(inp):
        tri = calc(points)

        if tri:
            print('YES {} {} {} {} {} {}'.format(tri[0][0], tri[0][1], tri[1][0], tri[1][1], tri[2][0], tri[2][1]))
        else:
            print('NO')
 
