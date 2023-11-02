
from typing import *
def sumOfSmallestAndSecondSmallest(n : int, arr: List[int]) -> int :
    ans = 0
    for i in range(1,n):
        if ans < arr[i] + arr[i-1]:
            ans = arr[i] + arr[i-1]
    return ans