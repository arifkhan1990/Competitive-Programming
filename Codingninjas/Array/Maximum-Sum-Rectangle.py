from os import *
from sys import *
from collections import *
from math import *


def kadaneSum(arr):
    curS , mxS = float('-inf'), float('-inf')
    for i in range(len(arr)):
        curS = max(arr[i], curS + arr[i])
        mxS = max(mxS, curS)

    return mxS

def maxSumRectangle(arr, n, m):
    ans = float('-inf')
    for k in range(m):
        newA = [0]*n
        for i in range(k,m):
            for j in range(n):
                newA[j] += arr[j][i]
            ans = max(ans, kadaneSum(newA))
    return ans