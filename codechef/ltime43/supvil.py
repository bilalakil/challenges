#!/usr/bin/env python

# https://www.codechef.com/LTIME43/problems/SUPVIL
# Passed.

import io
import sys

def test_data():
    '''
    Expected results:

    superheroes
    villains
    draw
    '''

    return io.StringIO(
'''3
2   
kittywoman  
wingman  
6  
hacker  
beautywoman  
blackjack  
noname  
watersnake  
strongman  
4  
famousman  
redsnake  
tallwoman  
tinythief  
'''
    )

def get_input(source):
    '''
    Generates lists of strings.
    '''

    with source as lines:
        t = int(next(lines))
        
        for _ in range(t):
            n = int(next(lines))
            combatants = []

            for _ in range(n):
                combatants.append(next(lines).strip())

            yield combatants

def fight_winner(combatants, win_threshold_superheroes, win_threshold_villains):
    '''
    Returns 'superheroes', 'villains' or 'draw'.
    '''

    swing = 0
    for combatant in combatants:
        swing += 1 if combatant[-3:] == 'man' else -1

        if swing == win_threshold_superheroes:
            return 'superheroes'
        elif swing == win_threshold_villains:
            return 'villains'

    return 'draw'

if __name__ == '__main__':
    win_threshold_superheroes = 2
    win_threshold_villains = -3
    inp = test_data() if '-test' in sys.argv else sys.stdin

    for combatants in get_input(inp):
       print(fight_winner(combatants, win_threshold_superheroes, win_threshold_villains))

