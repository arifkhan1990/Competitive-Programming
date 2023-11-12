from os import *
from sys import *
from collections import *
from math import *

def maximumSum(nums, k):
    n = len(nums)
    dp = [-1]*n
    ans = -1

    for i in range(n):
        dp[i] = [-1]*(k+1)
    
    for i in range(n):
        dp[i][1] = nums[i]
    

    for i in range(1, n):
        for j in range(i):

            if nums[j] <= nums[i]:
                for l in range(1, k):
                    if dp[j][l] != -1:
                        dp[i][l+1] = max(dp[i][l+1], dp[j][l] + nums[i])
    
    for i in range(n):
        if ans <= dp[i][k]:
            ans = dp[i][k]
    return  ans