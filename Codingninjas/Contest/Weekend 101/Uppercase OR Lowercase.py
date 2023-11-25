from typing import List

def uppercaseORLowercase(n: int, s: str) -> str:
    u, l = 0, 0
    for i in s:
        if i.isupper():
            u += 1
        else:
            l += 1
    return s.upper() if u > l else s.lower()