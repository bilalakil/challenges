#!/usr/bin/env python

# https://www.codechef.com/COOK92A/problems/CO92REST
# Did my best, but am still missing something.
import io
import sys

def test_data():
    '''
    Expected output:

    1
    8
    0
    1
    0
    900
    1
    0
    0
    0
    '''

    return io.StringIO('''10
4 2 10
2 3 5 4
I 1 2 
D 3 4
5 2 10
-1 -1 -1 -1 -1
I 1 3
D 3 5
6 2 2
-1 -1 -1 -1 -1 -1
I 1 4
D 4 6
5 2 10
-1 2 3 -1 1
I 1 3
D 3 5
5 2 10
-1 2 -1 -1 2
I 1 3
D 3 5
9 4 10
-1 2 -1 1 -1 -1 -1 -1 -1
I 4 5
D 5 6
I 7 8
D 8 9
3 1 2
3 -1 -1
D 1 3
3 1 2
2 -1 -1
D 1 3
3 1 2
-1 -1 -1
I 1 3
2 1 1
2 -1
D 1 2''')

def get_input(source):
    '''
    Generates a tuple (N, M, K, A, R) for each test case,
    where A is a list of integers,
    and C is a list of restrictions (constraints) in the form (T, L, R) -
    where T is the string "I" or "D".
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n, m, k = map(int, next(lines).split(' '))
            a = list(map(int, next(lines).split(' ')[:n]))

            c = []
            for _ in range(m):
                t, l, r = next(lines).strip().split(' ')
                c.append((t, int(l), int(r),))

            yield (n, m, k, a, c,)

class SolveException(Exception):
    pass

def calc(n, m, k, a, c,):
    '''
    Returns an integer.
    '''
    
    class Solver:
        def __init__(self, prev):
            self.delta = 0

            if prev == None or prev == -1:
                self.min = 1
                self.max = k
                self.locked = False
            else:
                self.min = self.max = prev
                self.locked = True

        def next(self, r, x):
            self.delta += 1 if r == 'I' else -1

            if x != -1:
                if not self.locked:
                    self.locked = True
                    self.min = self.max = x - self.delta
                elif x != self.min + self.delta:
                    raise SolveException()

            if self.locked:
                if self.min + self.delta < 1 or self.max + self.delta > k:
                    raise SolveException()
            else:
                self.min = max(self.min, 1 - self.delta)
                self.max = min(self.max, k - self.delta)

                if self.min > self.max:
                    raise SolveException()

        def possibilities(self):
            return self.max - self.min + 1

    rs = [None] * n
    for t, l, r in c:
        rs[l:r] = [t] * (r - l)

    cur_solver = None

    ans = 1

    def add_mod(x):
        nonlocal ans

        ans = (ans * x) % (10 ** 9 - 7)

    try:
        prev = None

        for i, x in enumerate(a):
            r = rs[i]

            if x > k:
                return 0

            if not r:
                if cur_solver:
                    add_mod(cur_solver.possibilities())
                    cur_solver = None

                if x == -1 and (i == n - 1 or rs[i + 1] == None):
                    add_mod(k)
            else:
                if cur_solver == None:
                    cur_solver = Solver(prev)

                cur_solver.next(r, x)

            prev = x

        if cur_solver != None:
            add_mod(cur_solver.possibilities())
    except SolveException:
        return 0

    return ans % (10 ** 9 - 7)
        
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
       print(calc(*args))
