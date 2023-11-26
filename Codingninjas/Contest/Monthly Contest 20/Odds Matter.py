from typing import *


def oddsMatter(n: int, a: List[int]) -> List[int]:
    e = []
    for i in range(1,n,2):
            e.append(a[i])
    return e