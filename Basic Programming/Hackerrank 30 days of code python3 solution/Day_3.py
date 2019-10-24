#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 3: Intro to Conditional Statements
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-conditional-statements/problem
#

import sys


N = int(input().strip())

if ((N>=2 and N < 6) or N > 20) and N%2==0 :
    print ('Not Weird')
else:
    print ('Weird')