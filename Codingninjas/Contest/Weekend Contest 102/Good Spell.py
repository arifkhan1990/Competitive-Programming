from typing import List

def goodSpell(n: int, s: str) -> int:
    s1 = s[:n//2]
    s2 = s[n//2:]
    p1,p2 = 1, 1

    for i in s1:
        p1 *= int(i)
    
    for i in s2:
        p2 *= int(i)
    return 1 if p1 == p2 else 0