from os import *
from sys import *
from collections import *
from math import *

def countDistinctElements(arr, k):
    # set solution
    ans = []
    for i in range(len(arr)-k+1):
        ans.append(len(set(arr[i:i+k])))
    return ans
