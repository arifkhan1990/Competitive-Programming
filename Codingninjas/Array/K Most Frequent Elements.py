from typing import List
from collections import *

def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    a = Counter(arr)
    b = sorted(a.items(), key=lambda x: x[1])
    ans = []
    for i in b[::-1]:
        if len(ans) == k:
            break
        ans.append(i[0])
    return ans


