#!/bin/python3

# https://www.hackerrank.com/contests/101hack51/challenges/charging-the-batteries
# Submitted successfully!

import sys
    
def calc(n, m, k, points):
    def dist(a):
        x, y = a
        
        if x == 0: return y
        elif y == n: return n + x
        elif x == n: return n * 3 - y
        else: return n * 4 - x
        
    dists = sorted(dist(p) for p in points)
    dists += list(map(lambda d: d + n * 4, dists[0:k]))
    
    min_dist = float('Inf')
    
    for i in range(m):
        min_dist = min(min_dist, dists[i + k - 1] - dists[i])
    
    return min_dist

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    points = []
    for a0 in range(m):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        points.append((x, y,))
    
    print(calc(n, m, k, points))

