from typing import *


def xySubstring(s: str) -> int:
    n = len(s)
    ans = 0

    for i in range(n):
        if s[i] == 'x' or s[i] == 'y':
            ans += 1
            for j in range(i+1,n):
                if s[j] == 'x' or s[j] == 'y':
                    ans += 1
                else:
                    break
    return ans