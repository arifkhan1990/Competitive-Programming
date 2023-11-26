from typing import List

def equalStrings(s: str, t: str) -> int:
    if len(s) != len(t):
        return 0
    
    if 'c' not in t:
        return 0
    return 1