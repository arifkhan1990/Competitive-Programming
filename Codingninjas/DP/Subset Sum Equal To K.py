from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    ans = [[0]*(k+1) for i in range(n+1)]
    ans[0][0] = 1
    for i in range(1,k+1):
        ans[0][i] = 0
    
    for i in range(1,n+1):
        for j in range(k+1):
            if arr[i-1] <= j:
                ans[i][j] = ans[i-1][j] + ans[i-1][j-arr[i-1]]
            else:
                ans[i][j] = ans[i-1][j]
    return ans[n][k]