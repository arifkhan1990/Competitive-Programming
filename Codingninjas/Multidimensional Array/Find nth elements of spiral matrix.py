from os import *
from sys import *
from collections import *
from math import *

def findKthElement(matrix, k):
    ans = []
    l, r = 0, len(matrix[0])
    t, b = 0, len(matrix)

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
    return ans[k-1]

