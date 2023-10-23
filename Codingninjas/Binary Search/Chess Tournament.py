from os import *
from sys import *
from collections import *
from math import *


def isStay(arr, m, c):
    l, cnt = 0, 1

    for i in range(1, len(arr)):
        if arr[i] - arr[l] >= m:
            cnt += 1
            l = i
        if cnt == c:
            return 1
    return 0
    
def chessTournament(positions, n , c):
    positions.sort()
    l, h = 1, positions[-1]
    while l <= h:
        m = l + (h-l) // 2
        if isStay(positions,m,c):
            l = m+1
        else:
            h = m-1
    return h
