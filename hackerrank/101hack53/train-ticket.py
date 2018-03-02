#!/bin/python3

# https://www.hackerrank.com/contests/101hack53/challenges/train-ticket
# Submission successful.

import os
import sys


def berthType(n):
    if (n-1) % 8 < 6:
        n = n % 8
        
        if n % 3 == 1:
            return 'LB'
        elif n % 3 == 2:
            return 'MB'
        else:
            return 'UB'
    elif n % 8 == 7:
        return 'SLB'
    else:
        return 'SUB'

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = berthType(n)

    f.write(result + '\n')

    f.close()

