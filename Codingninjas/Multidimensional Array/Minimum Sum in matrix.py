from os import *
from sys import *
from collections import *
from math import *

def minSum(arr):
    r = len(arr)
    c = len(arr[0])
    ans = []
    for i in range(r):
        x = []
        for j in range(c):
            x.append(0)
        ans.append(x)
    
    for i in range(c):
        ans[0][i] = arr[0][i]

    for i in range(1,r):
        ans[i][0] = min(ans[i-1][1], ans[i-1][2])+arr[i][0]
        ans[i][1] = min(ans[i-1][0], ans[i-1][2])+arr[i][1]
        ans[i][2] = min(ans[i-1][0], ans[i-1][1])+arr[i][2]
        
    return min([ans[r-1][0], ans[r-1][1], ans[r-1][2]])