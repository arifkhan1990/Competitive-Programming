from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def candies(N, K):
    ans = [0]*K
    i = 0
    while N:
        candis = min(N, i+1)
        ans[i%K] += candis
        N -= candis
        i += 1
    return ans


# Taking input using fast I/O
def takeInput():
    N = int(input())
    K = int(input())
    
    return N, K
    

# Main
t = int(input())
while t:
    N, K = takeInput()
    result = candies(N, K)
    print(*result)
    t = t-1