from os import *
from sys import *
from collections import *
from math import *

import sys
from sys import stdin

def spiralPathMatrix(matrix, n, m):
    ans = []
    l, r = 0 , m
    t, b = 0, n

    while l < r and t < b:

        for i in range(l, r):
            ans.append(matrix[t][i])
        t += 1
        
        for i in range(t, b):
            ans.append(matrix[i][r-1])
        r -= 1

        if not (l < r and t < b):
            break
        
        for i in range(r-1, l-1, -1):
            ans.append(matrix[b-1][i])
        b -= 1

        for i in range(b-1, t-1, -1):
            ans.append(matrix[i][l])
        l += 1

    return ans

t = int(input().strip())

for j in range(t):
    
    n, m = list(map(int, stdin.readline().strip().split(" ")))
    
    arr = []
    
    for i in range(n):
        
        a = list(map(int, stdin.readline().strip().split(" ")))
        arr.append(a)
            
    for i in spiralPathMatrix(arr, n, m):
        print(i, end = " ")
        
    print()