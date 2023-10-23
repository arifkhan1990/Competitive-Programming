from os import *
from sys import *
from collections import *
from math import *

def missingNumber(arr, n):
    dif = (arr[-1] - arr[0])//n
    l,h = 0,n-1
    ans = -1
    while l <= h:
        m = l + (h-l)//2
        t = arr[0] + (m*dif)

        if arr[m] != t:
            h = m-1
            ans = t
        else:
            l = m+1
    return ans