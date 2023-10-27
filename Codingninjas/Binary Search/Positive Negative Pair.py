from os import *
from sys import *
from collections import *
from math import *


'''
    Time Complexity     :   O(N * log(N))
    Space Complexity    :   O(N)

    Where 'N' is the size of the array.
'''

def find(arr, l, h, t):

    while l <= h:
        m = l + ( h - l)//2
        if arr[m] == t:
            return 1
        elif arr[m] > t:
            h = m - 1
        else:
            l = m + 1
    return 0

def pairs(arr, n):
    arr.sort()
    ans = []
    for i in arr:
        if i < 0:
            s = find(arr, 0, n-1, i*-1)
            if s != 0:
                ans.append([i,i*-1])
    return ans