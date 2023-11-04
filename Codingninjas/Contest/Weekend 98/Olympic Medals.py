from typing import List
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def check(pri,madel):
    for i in range(3):
        if pri[i] != madel[i]:
            return 0
    return 1

def recursiveCheck(pri, madel,prizes, i, n):
    if i == n:
        return 0
    pri[0] -= prizes[i][0]
    pri[1] -= prizes[i][1]
    pri[2] -= prizes[i][2]
    if check(pri, madel):
        return 1
    return recursiveCheck(pri, madel, prizes, i+1, n)


def possibleOrNot(n: int, g: int, s: int, b: int, prizes: List[List[int]]) -> int:
    pri = [0]*3
    for p in prizes:
        pri[0] += p[0]
        pri[1] += p[1]
        pri[2] += p[2]
        ch = check(pri, [g,s,b])
        if ch:
            return 1
    ch = recursiveCheck(pri, [g,s,b], prizes,0,n)
    if ch:
        return 1

    p1 = [0]*3
    p2 = [0]*3
    l = 0
    for p in prizes:
        p1[0] += p[0]
        p1[1] += p[1]
        p1[2] += p[2]
        
        if p2[0] + p[0] < g:
            p2[0] += p[0]
            p2[1] += p[1]
            p2[2] += p[2]
            ch = check(p2, [g,s,b])
            if ch:
                return 1
        else:
            p2.clear()
            p2 = [0]*3
            p2[0] += p[0]
            p2[1] += p[1]
            p2[2] += p[2]
            ch = check(p2, [g,s,b])
            if ch:
                return 1


        if p1[0] > g:
            p1[0] -= prizes[l][0]
            p1[1] -= prizes[l][1]
            p1[2] -= prizes[l][2]
            ch = check(p1, [g,s,b])
            if ch:
                return 1
    return 0
