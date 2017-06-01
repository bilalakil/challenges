#!/usr/bin/env python
 
# https://www.codechef.com/SNCKQL17/problems/SNELECT
# Submitted successfully!
 
import io
import sys
 
def test_data():
    '''
    Expected answers:
 
    mongooses
    tie
    tie
    snakes
    tie
    tie
    '''
 
    return io.StringIO('''6
sm
ssm
sms
ssmmmssss
mss
msmsss''')

def get_input(source):
    '''
    Returns a tuple (s,).
    '''
 
    with source as lines:
        t = int(next(lines))
 
        for _ in range(t):
            s = next(lines).strip()
 
            yield (s,)
 
def calc(s):
    count = 0
    n = len(s)

    for i in range(n):
        c = s[i]

        if c == 's':
            count += 1
        elif c == 'm':
            if i != 0 and s[i - 1] == 's':
                count -= 2
            else:
                count -= 1

                if i != n - 1 and s[i + 1] == 's':
                    s = s[:i + 1] + '.' + s[i + 2:]

    return 'tie' if count == 0 else ('snakes' if count > 0 else 'mongooses')
 
if __name__ == '__main__':
    inp = test_data() if '-test' in sys.argv else sys.stdin
 
    for args in get_input(inp):
        print(calc(*args))
 
