from os import *
from sys import *
from collections import *
from math import *

def findSubmatrixSum(arr, queries):
    ans = []
    for k in queries:
        s = 0
        for i in range(k[0], k[2]+1):
            for j in range(k[1], k[3]+1):
                s += arr[i][j]
        ans.append(s)
    return ans
