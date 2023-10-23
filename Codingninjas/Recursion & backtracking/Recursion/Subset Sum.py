

from typing import List

def solve(arr, i, n, ans, sm):
    if i == n:
        ans.append(sm)
        return ans
    solve(arr, i+1, n, ans, sm)
    solve(arr, i+1, n, ans, sm+arr[i])
    
def subsetSum(num: List[int]) -> List[int]:
    ans = []
    solve(num, 0, len(num), ans, 0)
    return sorted(ans)