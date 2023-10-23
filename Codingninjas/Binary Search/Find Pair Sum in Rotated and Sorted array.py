from os import *
from sys import *
from collections import *
from math import *


def findPairSum(arr, target):
    i, n = 0, len(arr)
    while i < n-1:
        if arr[i] > arr[i+1]:
            break
        i += 1
    l, r = (i+1)%n, i

    while l != r:
        s = arr[l]+arr[r]
        if s == target:
            return 1
        elif s > target:
            r = (n+r-1)%n
        else:
            l = (l+1)%n
    return 0