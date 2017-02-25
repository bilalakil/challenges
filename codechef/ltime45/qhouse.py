#!/usr/bin/env python

# https://www.codechef.com/LTIME45/problems/QHOUSE
# 2 out of 12 test cases wrong.
#
# Couldn't figure out a clean binary search implementation in time,
# considering this 'YES' 'NO' situation
# as opposed to the traditional needle in the haystack.
#
# That meant there were too many edge cases in the implementation,
# and they had some great test cases to catch them out.

import io
import sys

import math

def get_test(p1, p2, p3, p4):
    '''
    Inputs and outputs:

    7 2 4 6 = 34
    1000 999 999 1000 = 1997002
    '''

    # Some calculations for the triangle.
    h = p1 - p3
    w = p4

    query = None
    def o(raw_query):
        nonlocal query
        query = tuple(map(int, raw_query.split(' ')[1:]))
        
    def i():
        nonlocal query
        x, y = query

        if y < p3:
            return 'YES' if abs(x) <= p2 else 'NO'
        elif y <= p1:
            lim_x = (h - (y - p3)) * (w / h)
            lim_y = h - abs(x) / (w / h) + p3

            return 'YES' if abs(x) <= lim_x and y <= lim_y else 'NO'
        else:
            return 'NO'

    return (i, o)

def calc(i, o, lim_x, lim_y):
    def binary(lo, hi, heading, asker):
        cur = math.ceil((lo + hi) / 2)
        mod = math.ceil((hi - cur) / 2)
        last = None

        while True:
            o(asker(cur))

            answer = i()

            if answer == 'YES':
                if not last:
                    last = cur
                elif heading == 1:
                    last = cur if cur > last else last
                else:
                    last = cur if cur < last else last

            cur += mod * heading * (1 if answer == 'YES' else -1)

            # Catch a hop case..
            # Edge cases are my demise.
            if cur == hi + 1:
                cur = hi - 1

            if mod == 0:
                return last

            mod = math.ceil(mod / 2) if mod != 1 else 0

        return lo

    p1 = binary(0, lim_y, 1, lambda m: '? 0 ' + str(m))
    p2 = binary(0, lim_x, 1, lambda m: '? ' + str(m) + ' 0')
    p3 = binary(0, p1, -1, lambda m: '? ' + str(p2 + 1) + ' ' + str(m))
    p4 = binary(p2, lim_x, 1, lambda m: '? ' + str(m) + ' ' + str(p3))

    return 2 * p2 * p3 + (p1 - p3) * p4

if __name__ == '__main__':
    lim_x = 1000
    lim_y = 1000

    i = o = None

    if '-test' in sys.argv:
        i, o = get_test(7, 2, 4, 6)
    else:
        test = False
        for arg in sys.argv:
            if arg.startswith('-test='):
                i, o = get_test(*tuple(map(int, arg[6:].split(','))))

                test = True

        if not test:
            i = lambda: next(sys.stdin).strip()
            o = lambda m: print(m) or sys.stdout.flush()

    print('! ' + str(calc(i, o, lim_x, lim_y)))
