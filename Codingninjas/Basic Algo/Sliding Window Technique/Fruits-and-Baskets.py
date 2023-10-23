from typing import List
from collections import *

def findMaxFruits(arr: List[int], n: int) -> int:
    ans = 0
    tr = {}

    l = r = 0

    while r < n:
        if arr[r] in tr:
            tr[arr[r]] += 1
        else:
            tr[arr[r]] = 1

        while len(tr) > 2:
            if tr[arr[l]] == 1:
                tr.pop(arr[l])
            else:
                tr[arr[l]] -= 1
            
            l += 1
        
        ans = max(ans, r - l +1)

        r += 1
    return ans

