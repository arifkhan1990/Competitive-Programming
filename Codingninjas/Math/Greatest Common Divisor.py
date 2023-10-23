
from sys import stdin,setrecursionlimit
setrecursionlimit(10**9 + 15)

def findGcd(x, y):
    if y == 0:
        return x
    return findGcd(y, x%y)
