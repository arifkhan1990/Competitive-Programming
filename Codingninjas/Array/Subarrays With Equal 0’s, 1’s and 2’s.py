from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countSubarrays(n: int, arr: List[int]) -> int:
    mp = {}
    mp[(0, 0)] = 1
    zc,oc,tc = 0,0,0

    ans = 0
    for i in range(n):
        if arr[i] == 0:
            zc += 1
        elif arr[i] == 1:
            oc += 1
        else:
            tc += 1
        
        tmp = (zc-oc, zc-tc)
        if tmp in mp:
            ans += mp[tmp]
            mp[tmp] += 1
        else:
            mp[tmp] = 1
    return ans

