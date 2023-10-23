
import sys
from sys import stdin

from sys import stdin,setrecursionlimit
setrecursionlimit(10**9 + 15)

def nthTermOfGP(n, a, r):
    d = 1000000007
    if n == 1:
        return a
    return nthTermOfGP(n-1,(a*r)%d,r)


t = int(sys.stdin.readline().strip())

while(t > 0):
    
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    
    t = t - 1
