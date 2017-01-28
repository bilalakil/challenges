#!/usr/bin/env python

# https://www.codechef.com/LTIME44/problems/SEGMENTQ
# Submission failed.
#
# The submission contained an error:
# I had forgotten about setting bits for new queries that were marked in the past.
#
# However, this wasn't that caused the submission to fail.
# Rather, a strange timeout occurred (TLE -1.000000), with 0 reported memory usage.
# The same issue occurred with other users.
#
# I'm trying to find out what that means, in case I'm handling IO incorrectly.
# It was noted in the question's description it's an "online problem".
# Works fine using stdin from my terminal.

import io
import sys

def test_data():
    '''
    Expected results:

    0
    2
    1
    0
    1
    '''

    return io.StringIO(
'''5 10
0 1 2
0 2 3
1 2
0 2 2
0 3 3
1 3
1 1
1 4
0 4 5
1 5
'''
    )

def get_input(source):
    '''
    First yields a tuple of integers N and Q.

    Then generates tuples with two parts:
    - an integer representing the type of query (0 or 1); and
    - a tuple with the arguments for that query:
        - two integers L and R for query 0; or
        - one integer P for query 1.

    Examples:

        (0, (1, 2,))
        (1, (2,))
    '''

    with source as lines:
        n, q = map(int, next(lines).split(' ')[:2])
        yield n, q

        for _ in range(q):
            nums = list(map(int, next(lines).split(' ')))

            if nums[0] == 0:
                yield (0, (nums[1], nums[2]))
            elif nums[0] == 1:
                yield (1, (nums[1],))

class Calculator:
    def __init__(self, n):
        self.n = n

        self.output_bitmask = 1
        self.pos_marks = [0 for _ in range(n)]
        self.pos_bitmasks = [0 for _ in range(n)]

        self.count = 1
        self.num_queries = 1

    def handle_query(self, query_type, query_args):
        '''
        Returns None or an integer, depending on the query type.
        '''

        if query_type == 0:
            self.new_segment(*query_args)

            return None
        elif query_type == 1:
            return self.mark_and_get_activated(*query_args)

    def new_segment(self, l, r):
        '''
        Returns None.
        '''

        l -= 1
        r -= 1

        # First check that we can in fact add it
        # (i.e. that at least one position is not marked.)
        good = False
        for i in range(l, r + 1):
            if self.pos_marks[i] == 0:
                good = True
                break
        if not good:
            return

        # Add a 0 bit to the output bitmask.
        self.output_bitmask = self.output_bitmask << 1

        # Add the necessary bits to all of the position bitmasks.
        for i in range(n):
            self.pos_bitmasks[i] = self.pos_bitmasks[i] << 1

            # Mark bits outside of the segment, or that are already marked.
            if self.pos_marks[i] == 1 or i < l or i > r:
                self.pos_bitmasks[i] = self.pos_bitmasks[i] | 1

        self.num_queries += 1

    def mark_and_get_activated(self, p):
        '''
        Returns an integer.
        '''

        p -= 1

        self.pos_marks[p] = 1
        self.pos_bitmasks[p] = 2 ** (self.num_queries - 1) - 1

        all_and = 2 ** self.n - 1
        for bitmask in self.pos_bitmasks:
            all_and = all_and & bitmask

        self.output_bitmask = self.output_bitmask | all_and

        new_count = bin(self.output_bitmask).count('1')
        diff = new_count - self.count

        self.count = new_count

        return diff

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    inp = get_input(inp)
    n, q = next(inp)

    calc = Calculator(n)

    for i in inp:
        val = calc.handle_query(*i)

        if val != None:
            print(val)
