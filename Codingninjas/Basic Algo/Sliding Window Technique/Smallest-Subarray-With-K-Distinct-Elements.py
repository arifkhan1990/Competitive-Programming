from typing import List

def smallestSubarrayWithKDistinct(arr: List[int], k: int) -> List[int]:
    ans = []
    mp = {}
    i , j, s , e = 0 , 0, 0 , len(arr)
    while i < len(arr):
        if arr[i] not in mp:
            mp[arr[i]] = 1
        else:
            mp[arr[i]] += 1
        i += 1
        
        while len(mp) == k:
            if (i - j - 1) < (e-s):
                s, e = j, i-1

            if mp[arr[j]] == 1:
                mp.pop(arr[j])
            else:
                mp[arr[j]] -= 1

            j += 1

    return [-1] if e == len(arr) else [s,e]