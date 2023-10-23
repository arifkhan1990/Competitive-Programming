from os import *
from sys import *
from collections import *
from math import *

def maxOne(arr):
    ans = 0
    one = 0
    for i in range(len(arr)):
        if one < sum(arr[i]):
            one = sum(arr[i])
            ans = i
    return ans