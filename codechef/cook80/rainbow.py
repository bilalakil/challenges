#!/usr/bin/env python

# https://www.codechef.com/COOK80/problems/RAINBOW
# Submitted successfully, with 14 seconds on the clock...
import io
import sys

def test_data():
    '''
    Expected output:

    3
    0
    0
    4
    '''

    return io.StringIO('''4
3
0 1 2
1 0 3
2 3 0
3
0 1 1
1 0 3
1 3 0
2
0 1
1 0
6
0 9 2 4 7 8
9 0 9 9 7 9
2 9 0 3 7 6
4 9 3 0 7 1
7 7 7 7 0 7
8 9 6 1 7 0''')

def get_input(source):
    '''
    Generates a tuple (r, b, p) for each test case.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            nums = []

            for _ in range(n):
                nums.append(list(map(int, next(lines).strip().split(' '))))

            yield (nums,)

def calc(nums):
    '''
    Returns a number.
    '''
    
    while True:
        uninteresting = -1
        p = -1

        for i in range(len(nums)):
            e = -1
            interesting = True

            for j in range(len(nums[i])):
                n = nums[i][j]

                if n == 0:
                    p = j;
                elif e == -1:
                    e = n

                if n != 0 and n != e:
                    interesting = False
                    break
            
            if interesting:
                uninteresting = i
                break

        if uninteresting == -1:
            break

        del nums[uninteresting]

        for n in nums:
            del n[p]

    return len(nums)

if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for args in get_input(inp):
        print(calc(*args))
