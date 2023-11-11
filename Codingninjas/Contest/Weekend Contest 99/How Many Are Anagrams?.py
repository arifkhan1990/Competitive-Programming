from typing import List

def howManyAreAnagrams(n: int, m: int, a: List[str], b: List[str]) -> List[int]:
    ans = [0]*m
    res = {}
    a1 = [""]*n
    b1 = [""]*m

    for i in range(n):
        x = ''.join(sorted(a[i]))
        a1[i] = x
    
    for i in range(m):
        x = ''.join(sorted(b[i]))
        b1[i] = x
    
    for i in range(m):
        for j in a1:
            if b1[i] == j:
                ans[i] += 1
    
    return ans