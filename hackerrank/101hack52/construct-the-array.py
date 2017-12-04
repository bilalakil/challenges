#!/bin/python3

# https://www.hackerrank.com/contests/101hack52/challenges/construct-the-array
# I think this ended up being correct, but to my surprise it's too slow.
# Definitely something for me to investigate further and reflect upon.

import sys

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    return (
        (k - 1) ** (n - 2) - 
        sum(
            (1 if i % 2 == 1 else -1) *
            (k - 1) ** (n - i)
            for i in range(3, n + (0 if x == 1 else 1))
        )
    ) % (10 ** 9 + 7)

if __name__ == "__main__":
    n, k, x = input().strip().split(' ')
    n, k, x = [int(n), int(k), int(x)]
    answer = countArray(n, k, x)
    print(answer)
