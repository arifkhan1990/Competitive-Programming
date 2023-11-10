from os import *
from sys import *
from collections import *
from math import *


def minDeletions(str):
    c = Counter(str)
    ans = [0 for i in range(len(str)+1)]
    res = 0

    for key, val in c.items():
        while ans[val] and val > 0:
            val -= 1
            res += 1
        ans[val] = 1
    return res