#!/bin/python3

# https://www.hackerrank.com/contests/hourrank-27/challenges/impressing-the-boss
# Submitted successfully!

import os
import sys

def canModify(a):
    '''
    Brute forced, considering the very small limits:
    20 test cases with a maximum of 20 elements in the list.
    '''

    for i in range(len(a)):
        new_a = a[:i] + a[i+1:]
        
        prev = -1
        good = True
        
        for n in new_a:
            if n < prev:
                good = False
                break
            
            prev = n
        
        if good:
            return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canModify(a)

        print(result)
