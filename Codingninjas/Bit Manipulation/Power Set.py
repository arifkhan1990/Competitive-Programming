from os import *
from sys import *
from collections import *
from math import *

def pwset(v):
    l = len(v)
    ans = []
    for i in range(2**l):
        res = []
        for j in range(l):
            if i& 1 << j:
                res.append(v[j])
        ans.append(res)
    return ans