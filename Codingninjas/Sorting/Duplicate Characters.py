
from collections import *


from typing import *

def duplicate_char(s: str, n: int):
    # Write your code here.
    a = Counter(s)
    ans = []
    for i in set(s):
        if a[i] > 1:
            ans.append([i, a[i]])
    ans.sort()
    return ans

