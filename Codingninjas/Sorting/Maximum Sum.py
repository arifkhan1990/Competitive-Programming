

from typing import *;

def maximumSum(a: List[int], n: int)-> int:
    m = 1000000007
    a.sort()
    ans = 0
    for i in range(n):
        ans += (i*a[i])%m
    return ans%m