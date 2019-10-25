#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 11: 2D Arrays
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem
#

#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
ans = []    
for i in range(0,4):
    for j in range(0,4):
        s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        ans.append(s)
print(max(ans))
        