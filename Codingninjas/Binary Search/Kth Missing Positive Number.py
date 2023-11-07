from typing import *

def missingK(vec: List[int], n: int, k: int) -> int:
    l, h = 0, n-1
    while l <= h:
        m = (l+h)//2

        ms = vec[m] - (m+1)
        if ms < k:
            l = m+1
        else:
            h = m-1
    return h+k+1