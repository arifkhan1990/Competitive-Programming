#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 20: Sorting
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-sorting/problem
#

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
num = 0
for i in range(n):
    for j in range(n-1):
        if(a[j] > a[j+1]):
            num += 1
            a[j],a[j+1] = a[j+1], a[j]
            
print("Array is sorted in {} swaps.".format(num))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))