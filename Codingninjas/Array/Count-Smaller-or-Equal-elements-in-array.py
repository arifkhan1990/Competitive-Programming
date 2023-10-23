from os import *
from sys import *
from collections import *
from math import *

def countSmallerOrEqual(a, b, n, m):
    b.sort()
    ans = []
    for i in range(n):
        ans.append(binarySearch(b,0, m-1, a[i]))
    return ans

def binarySearch(arr, l, h, t):
    ans = 0
    while l <= h:
    
        m = l + (h-l) // 2

        if arr[m] <= t:
            ans =  m + 1
            l = m + 1
        else:
            h = m - 1
    return ans
