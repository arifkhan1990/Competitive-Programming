from os import *
from sys import *
from collections import *
from math import *

def checkDuplicate(arr, n, k):
    ans = set()
    l = 0
    for i in range(n):
        if i - l > k:
            ans.remove(arr[l]) 
            l += 1
        if arr[i] in ans:
            return True
        else:
            ans.add(arr[i])
    return False
