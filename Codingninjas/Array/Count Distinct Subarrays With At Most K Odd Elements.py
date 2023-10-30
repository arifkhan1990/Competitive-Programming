from typing import List

def solve(arr, k):
    n = len(arr)
    ans = 0
    j = 0
    o = 0
    for i in range(n):
        if arr[i]%2 == 1:
            o += 1

        while j <= i and o > k:
            if arr[j] % 2 == 1:
                o -= 1
            j += 1
    
        ans += i - j + 1
    return ans
def distinctSubKOdds(arr: List[int], k: int) -> int:
    return solve(arr,k) - solve(arr, k-1)