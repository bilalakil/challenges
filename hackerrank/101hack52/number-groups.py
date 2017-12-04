#!/bin/python3

# https://www.hackerrank.com/contests/101hack52/challenges/number-groups
# Submitted successfully!

import sys

def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    fi = k - 1
    f = (fi * (fi + 1) // 2) * 2 + 1
    
    return f * k + (2 * fi * (fi + 1)) // 2

if __name__ == "__main__":
    k = int(input().strip())
    answer = sumOfGroup(k)
    print(answer)
