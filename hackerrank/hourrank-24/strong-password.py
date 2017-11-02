#!/bin/python3

# https://www.hackerrank.com/contests/hourrank-24/challenges/strong-password
# Submitted successfully!

import sys
import re

target_length = 6

numbers = re.compile("[0123456789]")
lower_case = re.compile("[abcdefghijklmnopqrstuvwxyz]")
upper_case = re.compile("[ABCDEFGHIJKLMNOPQRSTUVWXYZ]")
special_characters = re.compile("[!@#$%^&*()\-+]")

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    num = 0 if numbers.search(password) else 1
    lower = 0 if lower_case.search(password) else 1
    upper = 0 if upper_case.search(password) else 1
    spec = 0 if special_characters.search(password) else 1
    
    return max(num + lower + upper + spec, target_length - n)

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
