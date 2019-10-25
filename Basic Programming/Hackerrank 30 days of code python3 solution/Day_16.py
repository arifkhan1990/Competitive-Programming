#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 16: Exceptions - String to Integer
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
#

import sys
try:
    print(int(input().strip()))
except ValueError:
    print('Bad String')