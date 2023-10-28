from os import *
from sys import *
from collections import *
from math import *

def removeDuplicates(arr):
    ans = {}
    res = []
    for i in arr:
        if i not in ans:
            ans[i] = 1
        else:
            ans[i] += 1
        if ans[i] == 1:
            res.append(i)
    return res


