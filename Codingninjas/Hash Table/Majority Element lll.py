from os import *
from sys import *
from collections import *
from math import *

def countTheNumber(arr, n, k):
    k = n//k
    a = Counter(arr)
    ans = []
    for i in set(arr):
        if a[i] >= k:
            ans.append(i)

    return ans