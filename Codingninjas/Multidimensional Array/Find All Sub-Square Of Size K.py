from os import *
from sys import *
from collections import *
from math import *

def sumOfKxKMatrices(arr:list, k:int):
    res = []
    n = len(arr)
    if k > n:
        return

    subSumMat = [[None] * n for i in range(n) ]

    for j in range(n):
        s = 0

        for i in range(k):
            s += arr[i][j]
        subSumMat[0][j] = s

        for i in range(1, n-k+1):
            s += arr[i+k-1][j] - arr[i-1][j]
            subSumMat[i][j] = s
    
    for i in range(n-k+1):
        s = 0
        rs = []
        for j in range(k):
            s += subSumMat[i][j]
        rs.append(s)
            
        
        for j in range(1,n - k +1):
            s += subSumMat[i][j+k-1] - subSumMat[i][j-1]
            rs.append(s)
        res.append(rs)
        

    return res

# def sumOfKxKMatrices(arr:list, k:int):

#     n = len(arr)

#     # This list of lists stores our answer.
#     ans = [[0 for i in range(n-k+1)] for j in range(n-k+1)]
    
#     # This list of lists stores our prefix sum of elements.
#     prefix = [[0 for i in range(n+1)] for j in range(n+1)]

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             # Calculating the prefix sums.
#             prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i - 1][j - 1]
        
#     for i in range(1,n-k+2):
#         for j in range(1,n-k+2):
#             # Using the formula as described in the explanation.
#             ans[i - 1][j - 1] = prefix[i + k - 1][j + k - 1] - prefix[i - 1][j + k - 1] - prefix[i + k - 1][j - 1] + prefix[i - 1][j - 1]

#     # Return the final answer.
#     return ans