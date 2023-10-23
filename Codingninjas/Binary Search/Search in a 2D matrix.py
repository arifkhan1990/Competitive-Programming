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

#  2nd way to solve the problem

# def findInMatrix(x, arr):

#     n = len(arr)
#     m = len(arr[0])

#     #    Binary search the complete matrix.
#     low = 0
#     high = (n - 1) * m + m - 1
    
#     while (low <= high):

#         mid = (low + high) // 2

#         #    Find the current element of the matrix.
#         row = mid // m
#         col = mid % m
        
#         #    Element found.
#         if (arr[row][col] == x):
#             return True
        
#         #    Reduce the search space
#         elif (arr[row][col] > x):
#             high = mid - 1

#         #    Reduce the search space.
#         else:
#             low = mid + 1

#     #    Element is not present in the matrix.
#     return False