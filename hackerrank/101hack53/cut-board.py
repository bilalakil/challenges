#!/bin/python3

# https://www.hackerrank.com/contests/101hack53/challenges/cut-board
# Partial solution (covering most test cases).
# I really tried to find out what was wrong :/

import os
import sys

import random

DEBUG = False
DEBUGCHARS = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

RANDOM_TRY = True
STOP_STDOUT = True
if DEBUG and RANDOM_TRY:
    if STOP_STDOUT:
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    have_tried = set()

TRY_FAILED = False

def fillBoard(n, m, x, y):
    numCells = n * m - x - y
    
    if numCells % 2 == 1:
        print('NO')
        return
    
    if x + y <= m:
        s1 = { 'sx': 1, 'sy': 2, 'w': x, 'h': n-1 }
        s2 = { 'sx': x+1, 'sy': 1, 'w': m - x - y, 'h': n }
        s3 = { 'sx': m+1 - y, 'sy': 1, 'w': y, 'h': n-1 }
    else:
        s1 = { 'sx': 1, 'sy': 2, 'w': m - y, 'h': n-1 }
        s2 = { 'sx': m+1 - y, 'sy': 2, 'w': x + y - m, 'h': n-2 }
        s3 = { 'sx': x+1, 'sy': 1, 'w': m - x, 'h': n-1 }
        
    if (s1['w'] * s1['h']) % 2 == 1 or (s2['w'] * s2['h']) % 2 == 1:
        print('NO')
        return
    
    print('YES')
    print(numCells // 2)
    
    if DEBUG:
        cells = {}
        counter = 1
    
    for section in [s1, s2, s3]:
        if section['w'] % 2 == 1:
            istep = 2
            jstep = 1
        else:
            istep = 1
            jstep = 2
        
        for i in range(section['sy'], section['sy'] + section['h'], istep):
            for j in range(section['sx'], section['sx'] + section['w'], jstep):
                print(i, j, i-1 + istep, j-1 + jstep)
                
                if DEBUG:
                    cells[(i, j,)] = counter
                    cells[(i-1 + istep, j-1 + jstep,)] = counter
                    counter += 1

    if DEBUG:
        numchars = len(DEBUGCHARS)
        goodCells = 0
        nonCells = 0
        
        print()
        print('DEBUG')
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                c = (i, j,)
                if c in cells:
                    goodCells += 1
                    print(DEBUGCHARS[(cells[c]-1) % numchars], end='')
                else:
                    print('_', end='')
                    nonCells += 1
            
            print()

        if nonCells != x + y or goodCells + nonCells != n * m:
            TRY_FAILED = True

if __name__ == '__main__':
    if not (DEBUG and RANDOM_TRY):
        n, m, x, y = map(int, input().split()[:4])

        fillBoard(n, m, x, y)
    else:
        while not TRY_FAILED:
            n = random.randrange(3, 100)
            m = random.randrange(3, 100)
            x = random.randrange(1, m-1)
            y = random.randrange(1, m-1)

            args = (n, m, x, y,)

            if args in have_tried:
                continue

            have_tried.add(args)

            fillBoard(*args)

            if STOP_STDOUT:
                old_stdout.write('.')
                old_stdout.flush()

        if STOP_STDOUT:
            old_stdout.write('\n')
            old_stdout.flush()
            
            sys.stdout = old_stdout
            fillBoard(*args)

