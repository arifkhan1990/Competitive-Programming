#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 7: Arrays
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-arrays/problem
#


import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(*reversed(arr))