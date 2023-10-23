from os import *
from sys import *
from collections import *
from math import *

def binarySearch(arr, l,h, t):
    if l > h:
        return -1
    
    while l <= h:
        m = l + (h-l) //2
        if arr[m] == t:
            return m
        elif arr[m] > t:
            h = m-1
        else:
            l = m+1
    return -1

def findInMatrix(x, arr):
    ans = -1
    for i in range(len(arr)):
        ans = binarySearch(arr[i], 0, len(arr[0])-1, x)
        if ans != -1:
            return 1
    return 0 if ans == -1 else 1

# 2nd way to solve the problem

# def findInMatrix(x, arr):

#     n = len(arr)
#     m = len(arr[0])
    
#     #    Initialize the two pointers.
#     i = 0
#     j = m - 1

#     while (i < n and j >= 0):
    
#         #    Element found.
#         if (arr[i][j] == x):
#             return True

#         #    Eliminate the current column.
#         elif (arr[i][j] > x):
#             j -= 1

#         #    Eliminate the current row.
#         else:
#             i += 1

#     #    Element is not present in the matrix.
#     return False