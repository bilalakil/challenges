#!/usr/bin/env python

# https://www.codechef.com/COOK80/problems/SPECIES
# Stuffed up the timezones (and alarm) - 1:15 after the competition ended.
# Submitted here: https://www.codechef.com/problems/SPECIES
# Wrong answers though; likely a bug in the merge -
# changed to a more logically fun question since the competition wasn't running anyway...
import io
import functools
import sys

def test_data():
    '''
    Expected output:

    1
    0
    6
    0
    288603514
    1
    0
    1
    '''

    return io.StringIO('''8
3
..?
.?B
G..
2
GG
..
3
?..
.??
??.
3
??P
???
??B
7
?.?.?.?
.?.?.?.
?.?.?.?
.?.?.?.
?.?.?.?
.?.?.?.
?.?.?.?
2
PP
PP
2
.?
G?
2
.?
P?''')

def get_input(source):
    '''
    Generates a tuple (G) is an array of strings (making the grid) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines).strip())

            g = []
            for _ in range(n):
                g.append(next(lines).strip())

            yield (g,)

class Field:
    def __init__(self):
        self.field = {}
        self.groups = set()

    def add(self, bear, x, y):
        cur = (x, y,)
        curG = Field.Group(bear)

        top = (x, y - 1,)
        left = (x - 1, y,)
        topG = None
        leftG = None

        if top in self.field:
            topG = self.field[top]
        if left in self.field:
            leftG = self.field[left]

        if topG and leftG:
            # Merge groups...
            topG.merge(leftG)
            
            self.field[left] = top
            if left in self.groups:
                self.groups.remove(left)

            topG.merge(curG)
            self.field[cur] = topG
        elif topG:
            # Add to top group...
            topG.merge(curG)
            self.field[cur] = topG
        elif leftG:
            # Add to left group...
            leftG.merge(curG)
            self.field[cur] = leftG
        else:
            # Create a new group.
            self.field[cur] = curG
            self.groups.add(cur)

    def num_permutations(self):
        mults = []

        for group in self.groups:
            group = self.field[group]

            if group.is_valid == False:
                return 0

            if group.unknowns == 0:
                mults.append(1)
            elif group.unknowns == 1:
                mults.append(1 if group.bear else 3)
            else:
                mults.append(1 if group.bear else 2)

        if len(mults) == 0:
            return 0

        return functools.reduce(lambda x, y: x * y, mults) % (10 ** 9 + 7)

    class Group:
        def __init__(self, bear):
            self.is_valid = True

            if bear == '?':
                self.unknowns = 1
                self.bear = None
            else:
                self.unknowns = 0
                self.bear = bear

        def merge(self, group):
            if self.bear == None and group.bear == None:
                self.unknowns += group.unknowns
            elif self.bear == 'G' or group.bear == 'G':
                self.is_valid = False
            elif self.bear == None or group.bear == None:
                if self.bear == None:
                    self.bear = group.bear
            elif self.bear != group.bear:
                self.is_valid = False

def calc(g):
    '''
    Returns a boolean.
    '''

    field = Field()
    n = len(g)

    for x in range(n):
        for y in range(n):
            bear = g[x][y]

            if bear == '.':
                continue

            field.add(bear, x, y)

    return field.num_permutations()

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
