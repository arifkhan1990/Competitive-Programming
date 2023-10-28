from typing import List

def replaceWithRank(arr: List[int],n : int) -> List[int]:
    # write your code here
    a = {}
    b = list(set(arr))
    b.sort()
    for i in range(len(b)):
        if b[i] not in a:
            a[b[i]] = i+1
    
    for i in range(n):
        arr[i] = a[arr[i]]

    return arr
    
