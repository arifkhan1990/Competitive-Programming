from os import *
from sys import *
from collections import *
from math import *

def subArrayCount(arr, k):
    # 10/10 test case pass
    ans = 0
    s = 0
    d = {0:1}
    for i in range(len(arr)):
        s += arr[i]
        r = s%k
        if r < 0:
            r += k
        if r in d:
            ans += d[r]
            d[r] += 1
        else:
            d[r] = 1
    return ans





# partially accepted 7/10 test case pass 
    # ans = 0
    # for i in range(len(arr)):
    #     s = 0
    #     for j in range(i,len(arr)):
    #         s += arr[j]
    #         if s%k == 0:
    #             ans += 1
    # return ans