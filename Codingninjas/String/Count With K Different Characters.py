'''
        Time Complexity: O(N ^ 2)
        Space complexity: O(1)

        Where N denotes the length of the given string.
'''

from typing import *

def countSubStrings(s: str, k: int) -> int:
    n = len(s)
    ans = 0
    

    for i in range(0,n):
        disC = 0
        cnt = [0]*27
        for j in range(i, n):
            if cnt[ord(s[j]) - 97] == 0:
                disC += 1
            cnt[ord(s[j]) - 97] += 1

            if disC == k:
                ans += 1
            if disC > k:
                break
    return ans