#!/usr/bin/env python

# https://www.codechef.com/COOK91/problems/CTHREE
import io
import sys

import math

def test_data():
    '''
    Expected output:

    10
    97800
    1
    '''

    return io.StringIO('''3
100 8 23 11
497296800 1000000 1000000 1000000
1 1 2 3''')

def get_input(source):
    '''
    Generates a tuple of integers (N, a, b, c) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, a, b, c = map(int, next(lines).split(' '))

            yield (n, a, b, c,)

# Thanks: https://stackoverflow.com/a/37058745/1406230
def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            if not i in factors:
                factors[i] = 0
            factors[i] += 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    yield from generate(0)

def brute_force(n, a, b, c):
    '''
    O(n) (considering the number of divisors is ~cube root(n)),
    but n is up to 10^9, so no bingo of course.

    Returns an integer.
    '''

    divs = sorted(list(divisors(n)))
    triples = 0

    for x in divs:
        if x > a: break
        for y in divs:
            if y > b: break
            for z in divs:
                if z > c: break
                if x * y * z == n: triples += 1

    return triples

def calc(n, a, b, c):
    '''
    Returns an integer.
    '''

    return -1
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
