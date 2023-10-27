from os import *
from sys import *
from collections import *
from math import *

def largestSquareSubmatrix(mat, n, m, k):
    ansSz = 0
    prefixSum = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1,n+1):
        for j in range(1, m+1):
            prefixSum[i][j] = mat[i-1][j-1]+prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]
    
    lo = 0
    hi = min(n,m)
    while lo <= hi :
        mid = lo + (hi -lo)//2
        isFound = 0

        for i in range(1,n-mid+2):
            for j in range(1, m-mid+2):
                s = prefixSum[i+mid-1][j+mid-1]-prefixSum[i+mid-1][j-1]-prefixSum[i-1][j+mid-1]+prefixSum[i-1][j-1]

                if s <=k :
                    isFound = 1
                    break
            if isFound:
                break
        
        if isFound:
            ansSz = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ansSz*ansSz

