#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 25: Running Time and Complexity
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
#

import math

def primecheck(n):
    x = int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i == 0:
            return False
    return True

n = int(input())
while n:
    x = int(input())
    print('Prime' if primecheck(x) and x >= 2 else 'Not prime')
    n -= 1