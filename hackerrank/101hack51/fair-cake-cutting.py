#!/bin/python3

# https://www.hackerrank.com/contests/101hack51/challenges/fair-cake-cutting
# Submitted successfully!

import sys

def howManyToInvite(A, B, a):
    return int(a / (A / B))

if __name__ == "__main__":
    A, B, a = input().strip().split(' ')
    A, B, a = [int(A), int(B), int(a)]
    b = howManyToInvite(A, B, a)
    print(b)

