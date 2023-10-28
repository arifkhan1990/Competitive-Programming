
from collections import *

from typing import *

def second_repeat(arr: List[str], n: int) -> str:
    # Write your code here.
    c = Counter(arr)
    mx = max(c.values())
    sx = 0
    ans = ""
    for i in c:
        if c[i] > sx and c[i] < mx:
            sx = c[i]
            ans = i
    return ans

